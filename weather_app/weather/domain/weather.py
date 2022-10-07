from dataclasses import dataclass


@dataclass
class Weather:
    id: str
    temperature: int
    city: str
