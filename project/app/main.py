from fastapi import FastAPI

from project.app.db import init_db
from project.app.api import coins

def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(
        coins.router, prefix='/coins', tags=["coins"]
    )

    return application


app = create_application()

@app.on_event("startup")
async def startup_event():
    init_db(app)