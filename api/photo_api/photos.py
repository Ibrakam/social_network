from api import app
from fastapi import Request, Body, UploadFile
from database.photoservice import *


@app.get('/api/photo/<int:photo_id>')
async def get_all_or_exact_photo(photo_id: int = 0, user_id: int = 0):
    if photo_id and user_id:
        all_or_exact_photo = get_all_or_exact_photo_db(photo_id, user_id)

        return {'status': 1, 'message': all_or_exact_photo}
    return {'status': 0, 'message': ''}


@app.put('/api/photo')
async def update_photo(photo_id: int = Body(...), photo_file: UploadFile = Body(...)):
    if photo_file:
        with open(f'{photo_id}.jpg', 'wb') as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)
        change_photo_db(photo_id, f'/api/photo_api/photos/{photo_id}.jpg')
        return {'status': 1, 'message': 'photo updated'}


@app.delete('/api/photo')
async def delete_photo(request: Request):
    data = await request.json()

    photo_id = data['post_id']

    if photo_id:
        delete_photo_db(photo_id)
        return {'status': 1, 'message': 'photo deleted'}
    return {'status': 0, 'message': 'not deleted'}
