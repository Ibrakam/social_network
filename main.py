from fastapi import FastAPI
from database import Base, engine

Base.metadata.create_all(bind=engine)


app = FastAPI()

from api.comment_api import comments
from api.hashtag_api import hashtags
from api.post_api import posts
from api.photo_api import photos
from api.user_api import users











# @app.get('/hello')
# async def hello():
#     return {'hello': 'FastAPI'}
#
# @app.post('/hello')
# async def post_home(name: str):
#     return {'message': f'Hello{name}'}
