from typing import Optional

from meta import Meta
from page import Page
from incident import Incident
from component import Component
from component_update import ComponentUpdate


class StatusPageResponse:
    meta: Meta
    page: Page
    component_update: Optional[ComponentUpdate]
    component: Optional[Component]
    incident: Optional[Incident]

    def __init__(self, meta: Meta, page: Page, component_update: Optional[ComponentUpdate], component: Optional[Component], incident: Optional[Incident]) -> None:
        self.meta = meta
        self.page = page
        self.component_update = component_update
        self.component = component
        self.incident = incident
