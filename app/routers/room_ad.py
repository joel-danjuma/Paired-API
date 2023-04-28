from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from .. import schemas, crud, oauth2
from typing import List

router = APIRouter(prefix="/rooms", tags=["Rooms"])


@router.get("/")
def get_all_ads(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
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
    new_post = crud.create_room_ad(user_id, ad, db)
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
    id: int,
    ad_: schemas.CreateRoomAd,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    ad_query = crud.get_room_ad_by_id(id, db)
    ad = ad_query.first()
    if ad == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ad with id: {id} does not exist.",
        )
    if ad.owner_id != current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Not authorized to perform action",
        )
    ad_query.update(ad_.dict(), synchronize_session=False)
    db.commit()
    return ad_query


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ad_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    ad_query = crud.get_room_ad_by_id(id, db)
    ad = ad_query.first()
    if get_ads_for_user == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ad with id: {id} does not exist.",
        )
    if ad.owner_id != current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Not authorized to perform action",
        )
    ad_query.delete(synchronize_session=False)
    db.commit()
