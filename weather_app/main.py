from typing import Union

from fastapi import FastAPI

from weather.delivery.router import router

app = FastAPI()
app.include_router(router)
