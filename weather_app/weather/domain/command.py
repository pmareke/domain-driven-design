from dataclasses import dataclass
from uuid import UUID


@dataclass
class Command:
    command_id: UUID
