from fastapi import FastAPI

from weather_app.weather.delivery.api.v1.weather.find_all_router import find_all_router
from weather_app.weather.delivery.api.v1.weather.find_one_router import find_one_router
from weather_app.weather.delivery.api.v1.weather.create_one_router import (
    create_one_router,
)
from weather_app.weather.delivery.api.v1.weather.delete_one_router import (
    delete_one_router,
)
from weather_app.weather.delivery.api.v1.weather.update_one_router import (
    update_one_router,
)
from weather_app.weather.delivery.api.v1.health import health_router

app = FastAPI()

app.include_router(health_router)
app.include_router(find_all_router)
app.include_router(find_one_router)
app.include_router(create_one_router)
app.include_router(delete_one_router)
app.include_router(update_one_router)
