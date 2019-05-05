from datetime import datetime


class IncidentUpdate:
    body: str
    created_at: datetime
    display_at: datetime
    status: str
    twitter_updated_at: None
    updated_at: datetime
    wants_twitter_update: bool
    id: str
    incident_id: str

    def __init__(self, body: str, created_at: datetime, display_at: datetime, status: str, twitter_updated_at: None, updated_at: datetime, wants_twitter_update: bool, id: str, incident_id: str) -> None:
        self.body = body
        self.created_at = created_at
        self.display_at = display_at
        self.status = status
        self.twitter_updated_at = twitter_updated_at
        self.updated_at = updated_at
        self.wants_twitter_update = wants_twitter_update
        self.id = id
        self.incident_id = incident_id
