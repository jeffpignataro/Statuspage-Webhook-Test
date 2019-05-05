
from datetime import datetime


class Meta:
    unsubscribe: str
    documentation: str

    def __init__(self, unsubscribe: str, documentation: str) -> None:
        self.unsubscribe = unsubscribe
        self.documentation = documentation
