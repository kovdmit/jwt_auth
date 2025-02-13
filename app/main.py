from fastapi import FastAPI

from routes import router
from services.db_services import init_db


init_db()


app = FastAPI()
app.include_router(router)
