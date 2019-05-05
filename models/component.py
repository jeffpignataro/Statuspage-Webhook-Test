from datetime import datetime


class Component:
    created_at: datetime
    id: str
    name: str
    status: str

    def __init__(self, created_at: datetime, id: str, name: str, status: str) -> None:
        self.created_at = created_at
        self.id = id
        self.name = name
        self.status = status
