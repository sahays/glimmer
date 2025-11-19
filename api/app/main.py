from app.dependencies import get_db
from app.routers import projects, users
from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

app = FastAPI(title="Glimmer API", version="0.1.0")

app.include_router(users.router)
app.include_router(projects.router)


@app.get("/")
async def root(db: Session = Depends(get_db)):
    # A simple query to test the database connection
    result = db.execute(text("SELECT 1")).scalar_one()
    return {"message": "Hello World", "db_connection_test": result}
