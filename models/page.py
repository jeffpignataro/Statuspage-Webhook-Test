class Page:
    id: str
    status_indicator: str
    status_description: str

    def __init__(self, id: str, status_indicator: str, status_description: str) -> None:
        self.id = id
        self.status_indicator = status_indicator
        self.status_description = status_description
