from typing import Dict
from fastapi import APIRouter

health_router = APIRouter()


@health_router.get("/api/v1/health")
def health() -> Dict[str, bool]:
    return {"ok": True}
