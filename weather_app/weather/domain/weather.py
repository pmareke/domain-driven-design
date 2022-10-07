import uuid
from dataclasses import dataclass


@dataclass
class Weather:
    id = uuid.uuid1()
    temperature: int
    city: str
