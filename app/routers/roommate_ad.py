from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from .. import schemas, crud, oauth2
from typing import List

router = APIRouter(prefix="/roommates", tags=["Posts"])


# get all ads
@router.get("/", response_model=List[schemas.RoommateAd])
def get_ads(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    user_id = current_user
    posts = crud.get_posts(user_id, db)
    return posts


# get ad by id
@router.get("/{id}", response_model=schemas.RoommateAd)
def get_ad_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    post = crud.get_post_by_id(id, db).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found.",
        )
    if post.owner_id != current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Not authorized to perform action",
        )
    return post


# create new ad
@router.post("/new", status_code=status.HTTP_201_CREATED)
def create_ad(
    ad: schemas.CreateRoommateAd,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    user_id = current_user
    new_post = crud.create_roommate_ad(user_id, ad, db)
    return new_post


# delete ad by id
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ad_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    post_query = crud.get_post_by_id(id, db)
    post = post_query.first()
    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ad with id: {id} does not exist.",
        )
    if post.owner_id != current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Not authorized to perform action",
        )
    post_query.delete(synchronize_session=False)
    db.commit()


# update ad by id
@router.put("/{id}")
def update_ad(
    id: int,
    ad: schemas.CreateRoommateAd,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    post_query = crud.get_post_by_id(id, db)
    if post_query.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ad with id: {id} does not exist.",
        )
    if post_query.first().owner_id != current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Not authorized to perform action",
        )
    post_query.update(ad.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
