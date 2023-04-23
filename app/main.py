from fastapi import FastAPI
from .database import engine
from . import models
from .routers import roommate_ad, user, auth, room_ad

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(roommate_ad.router)
app.include_router(room_ad.router)
app.include_router(user.router)
app.include_router(auth.router)


# Root page for the api
@app.get("/")
def root():
    return {"message": "Welcome to my API"}
