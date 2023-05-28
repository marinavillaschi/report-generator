from fastapi import APIRouter

from api import schemas
from api.services import generator_service

generate_router = APIRouter()


@generate_router.post("/csv", response_model=schemas.GeneratorOutput)
def generate_csv(input_data: schemas.GeneratorInput):

    print(f"generating data for date: {input_data.day}")

    return generator_service.generate_csv(input_data.day)
