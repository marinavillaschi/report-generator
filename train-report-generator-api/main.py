import uvicorn
from decouple import config
from fastapi import FastAPI

from api.router import api_router

API_HOST = config("API_HOST")
API_PORT = config("API_PORT", cast=int)


def start_api(api):

    app = FastAPI(
        title="report-generator",
        description="Train Report Generator API",
        version="1.0.0",
    )

    app.include_router(api, prefix="/api/v1")

    uvicorn.run(app, host=API_HOST, port=API_PORT)


if __name__ == "__main__":
    start_api(api_router)
