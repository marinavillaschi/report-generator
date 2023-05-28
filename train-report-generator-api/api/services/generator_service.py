from datetime import datetime

import pandas as pd
from decouple import config
from fastapi import HTTPException

FILE_PATH = config("FILE_PATH")


def generate_csv(day):
    start = datetime.now()

    try:
        df_sandbox = pd.read_csv(FILE_PATH)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail={
                "error": "true",
                "message:": "Can't read file.",
            },
        ) from exc

    end = datetime.now()

    return {
        "filename": "Workout.csv",
        "day": day,
        "rows": df_sandbox.shape[0],
        "columns": df_sandbox.shape[1],
        "runtime_seconds": end - start
    }
