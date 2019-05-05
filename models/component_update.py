from datetime import datetime


class ComponentUpdate:
    created_at: datetime
    new_status: str
    old_status: str
    id: str
    component_id: str

    def __init__(self, created_at: datetime, new_status: str, old_status: str, id: str, component_id: str) -> None:
        self.created_at = created_at
        self.new_status = new_status
        self.old_status = old_status
        self.id = id
        self.component_id = component_id
