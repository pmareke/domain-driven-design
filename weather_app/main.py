from fastapi import FastAPI

from weather.delivery.api.v1.router import router as router_v1

app = FastAPI()

app.include_router(router_v1)
