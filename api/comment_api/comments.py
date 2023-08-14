from api import app
from fastapi import Request
from database.postservice import get_exact_post_comment, post_comment, change_exact_comment, delete_comment

@app.get('/api/comment')
async def get_exact_post_comments(request: Request):
    data = await request.json()

    post_id = data.get('post_id')
    if post_id:
        exact_post_comments = get_exact_post_comment(post_id)

        return {'status': 1, 'message': exact_post_comments}
    return {'status': 0, 'message': 'неверный ввод данных'}


@app.post('/api/comment')
async def public_comment():
    pass

@app.put('/api/comment')
async def change_exact_user_comment():
    pass

@app.delete('/api/comment')
async def delete_exact_user_comment():
    pass

