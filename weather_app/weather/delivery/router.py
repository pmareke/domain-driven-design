from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    return {"ok": True}


@router.get("/api/v1/weather")
def weather():
    return {
        "weathers": [{
            "temperature": 30,
            "city": "Madrid",
        }, ]
    }


@router.get("/api/v1/weather/{city_id}")
def weather_by_city(city_id: int):
    return {
        "weather": {
            "temperature": 30,
            "city": "Madrid",
        }
    }
