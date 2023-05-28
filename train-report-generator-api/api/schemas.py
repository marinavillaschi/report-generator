from datetime import date, datetime, timedelta

from pydantic import BaseModel, validator


class GeneratorInput(BaseModel):
    day: date

    @validator("day", pre=True, always=True)
    def validate_date_input(cls, value):
        return datetime.strptime(str(value), "%Y-%m-%d").date()

    class Config:
        schema_extra = {
            "example": {
                "day": "2022-12-29",
            }
        }


class GeneratorOutput(BaseModel):
    filename: str
    day: date
    rows: int
    columns: int
    runtime_seconds: timedelta
