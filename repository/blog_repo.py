from sqlalchemy.orm import Session

import models
import schemas
from utils import exceptions


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, user_id: int, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_by_id(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise exceptions.not_found("blog not found")
    return blog


def update(id: int, request: schemas.Blog, user_id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    check_validity(blog, user_id)
    blog.title = request.title
    blog.body = request.body
    db.add(blog)
    db.commit()
    return 'updated'


def delete(id: int, user_id: int, db: Session):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    check_validity(blog_query.first(), user_id)
    blog_query.delete(synchronize_session=False)
    db.commit()
    return 'deleted'


def check_validity(blog: models.Blog, user_id: int):
    if not blog:
        raise exceptions.not_found("blog not found")
    if blog.user_id != user_id:
        raise exceptions.not_allowed()
