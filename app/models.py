from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    occupation = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )


class RoommateAd(Base):
    __tablename__ = "roommate_ads"

    id = Column(Integer, primary_key=True, nullable=False)
    gender = Column(String, nullable=False)
    budget = Column(Integer, nullable=False)
    pets = Column(Boolean, server_default="FALSE", nullable=False)
    smoking = Column(Boolean, server_default="FALSE", nullable=False)
    # move_in_date = Column(String, nullable=False)
    available_from = Column(String, nullable=False)
    owner_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )


class RoomAd(Base):
    __tablename__ = "room_ads"

    id = Column(Integer, primary_key=True, nullable=False)
    location = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    bedrooms = Column(Integer, nullable=False)
    smoking = Column(Boolean, server_default="FALSE", nullable=False)
    pets = Column(Boolean, server_default="FALSE", nullable=False)
    available_from = Column(String, nullable=False)
    owner_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
