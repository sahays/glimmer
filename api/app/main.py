from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from .database import SessionLocal

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root(db: Session = Depends(get_db)):
    # A simple query to test the database connection
    result = db.execute(text("SELECT 1")).scalar_one()
    return {"message": "Hello World", "db_connection_test": result}
