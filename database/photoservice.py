from database import get_db
from database.models import Photo

def get_all_or_exact_photo_db(photo_id, user_id):
    db = get_db()
    if user_id:
        exact_photo = db.query(Photo).filter_by(user_id=user_id).all()

        return {'status': 1, 'message': exact_photo}

    elif photo_id:
        exact_photo = db.query(Photo).filter_by(id=photo_id).first()

        return {'status': 1, 'message': exact_photo}
    else:
        all_photos = db.query(Photo).all()

        return {'status': 0,'message': all_photos}



def change_photo_db(photo_id, new_photo):
    db = get_db()
    photo = db.query(Photo).filter_by(id=photo_id).first()

    if photo:
        photo.photo_path = new_photo
        db.commit()
        return True
    return False

def delete_photo_db(photo_id):
    db = get_db()
    photo = db.query(Photo).filter_by(id=photo_id).first()

    if photo:
        db.delete(photo)
        db.commit()
        return 'фото удалено'
    return 'фото не найдено'







