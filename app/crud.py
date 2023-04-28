from . import models, schemas
from sqlalchemy.orm import Session


# ROOMATE ADS
def create_roommate_ad(user_id: int, ad: schemas.CreateRoommateAd, db: Session):
    new_ad = models.RoommateAd(owner_id=user_id, **ad.dict())
    db.add(new_ad)
    db.commit()
    db.refresh(new_ad)
    return new_ad


def get_roommate_ads(user_id: int, db: Session):
    return (
        db.query(models.RoommateAd).filter(models.RoommateAd.owner_id == user_id).all()
    )


def get_roommate_ads_by_id(id: int, db: Session):
    return db.query(models.RoommateAd).filter(models.RoommateAd.id == id)


# USERS
def create_user(user: schemas.CreateUser, db: Session):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    return db.query(models.User).all()


def get_user_by_email(email: str, db: Session):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_id(id: int, db: Session):
    return db.query(models.User).filter(models.User.id == id)


# ROOM_ADS
def create_room_ad(user_id: int, ad: schemas.CreateRoomAd, db: Session):
    new_ad = models.RoomAd(owner_id=user_id, **ad.dict())
    db.add(new_ad)
    db.commit()
    db.refresh(new_ad)
    return new_ad


def get_all_room_ads(db: Session):
    return db.query(models.RoomAd).all()


def get_all_room_ads_for_user(user_id: int, db: Session):
    return db.query(models.RoomAd).filter(models.RoomAd.owner_id == user_id).first()


def get_room_ad_by_id(id: int, db: Session):
    return db.query(models.RoomAd).filter(models.RoomAd.id == id)
