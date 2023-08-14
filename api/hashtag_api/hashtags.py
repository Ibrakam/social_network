from api import app
from database.postservice import get_exact_hashtags, get_hashtags


@app.get('/api/hashtag')
async def get_some_hashtags(size: int=20, page: int=1):
    pass

@app.get('/api/hashtag/<str:hashtag_name>')
async def get_exact_hashtag(hashtag_name: str):
    if hashtag_name:
        exact_hashtags = get_exact_hashtags(hashtag_name)

        return {'status': 1, 'message': exact_hashtags}

    return {'status': 0,'message': 'No hashtag provided'}

