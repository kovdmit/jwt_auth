from fastapi import FastAPI

from routes import router
from services.db_services import init_db

app = FastAPI()

init_db()

app.include_router(router)
