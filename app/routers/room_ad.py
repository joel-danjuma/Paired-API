from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from .. import schemas, crud, oauth2
from typing import List

router = APIRouter(prefix="/rooms", tags=["Rooms"])


@router.get("/")
def get_all_ads(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_admin)
):
    room_ads = crud.get_all_room_ads(db)
    return room_ads


@router.post("/")
def create_ad(
    ad: schemas.CreateRoomAd,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    user_id = current_user
    new_post = crud.create_post(user_id, ad, db)
    return new_post


@router.get("/")
def get_ads_for_user(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    user_id = current_user
    user_ads = crud.get_all_ads_for_user(user_id, db)
    return user_ads


@router.put("/{id}")
def update_ad_by_id(
    ad_id: int,
    ad: schemas.CreateRoomAd,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    ad_query = crud.get_post_by_id(ad_id, db).first()
    if ad_query == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ad with id: {id} does not exist.",
        )
    if ad_query.owner_id != current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Not authorized to perform action",
        )
    ad_query.update(ad)
    db.commit()
    return ad_query


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ad_by_id(
    ad_id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    post_query = crud.get_post_by_id(ad_id, db)
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
