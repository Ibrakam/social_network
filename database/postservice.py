from database.models import UserPost, Comment, HashTag
from database import get_db
from datetime import datetime


def get_all_or_exact_post(post_id):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(id=post_id).first()

    if post_id == 0:
        return db.query(UserPost).filter_by(id=post_id).all()
    return exact_post


def change_post_data(post_id, change_info, new_data):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(id=post_id).first()

    if exact_post:
        if change_info == 'main_text':
            exact_post.main_text = new_data
        db.commit()

        return 'Correct'
    return 'don`t correct'


def delete_post(post_id):
    db = next(get_db())

    deletepost = db.query(UserPost).filter_by(id=post_id).first()

    if deletepost:
        db.delete(deletepost)
        db.commit()
        return 'Deleted'
    return 'not deleted'


def get_exact_post_comment(post_id):
    db = next(get_db())

    exact_comment = db.query(Comment).filter_by(post_id=post_id).all()

    if exact_comment:
        return exact_comment
    return []


def post_comment(post_id, user_id, text):
    db = next(get_db())

    new_comment = Comment(post_id=post_id, user_id=user_id, text=text, reg_date=datetime.now())
    db.add(new_comment)
    db.commit()

    return new_comment.id


def change_exact_comment(comment_id, new_comment_text):
    db = next(get_db())

    exact_comment = db.query(Comment).filter_by(id=comment_id).first()

    if exact_comment:
        exact_comment.text = new_comment_text
        db.commit()
        return 'Changed'
    return 'Not found'


def delete_comment(comment_id):
    db = next(get_db())

    deletecomment = db.query(Comment).filter_by(id=comment_id).first()
    if deletecomment:
        db.delete(deletecomment)
        db.commit()

        return 'Deleted'
    return 'not found'


def get_hashtags(size):
    db = next(get_db())

    hashtag = db.query(HashTag).all()

    return hashtag[:size]


def get_exact_hashtags(hashtag_name):
    db = next(get_db())

    exact_hashtag = db.query(HashTag).filter_by(hashtag_name=hashtag_name).first()
    if exact_hashtag:
        return exact_hashtag.id

    return []



