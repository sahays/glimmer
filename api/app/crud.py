from app import models, schemas
from sqlalchemy.orm import Session

# --- User Operations ---


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_google_id(db: Session, google_id: str):
    return db.query(models.User).filter(models.User.google_id == google_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        email=user.email,
        google_id=user.google_id,
        full_name=user.full_name,
        picture_url=user.picture_url,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# --- Project Operations ---


def get_projects(db: Session, skip: int = 0, limit: int = 100, owner_id: int = None):
    query = db.query(models.Project)
    if owner_id:
        query = query.filter(models.Project.owner_id == owner_id)
    return query.offset(skip).limit(limit).all()


def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.project_id == project_id).first()


def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(
        project_name=project.project_name,
        owner_id=project.owner_id,
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def delete_project(db: Session, project_id: int):
    db_project = db.query(models.Project).filter(models.Project.project_id == project_id).first()
    if db_project:
        db.delete(db_project)
        db.commit()
        return True
    return False
