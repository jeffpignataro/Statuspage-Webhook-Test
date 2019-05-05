from datetime import datetime
from typing import List

from incident_update import IncidentUpdate


class Incident:
    backfilled: bool
    created_at: datetime
    impact: str
    impact_override: None
    monitoring_at: datetime
    postmortem_body: None
    postmortem_body_last_updated_at: None
    postmortem_ignored: bool
    postmortem_notified_subscribers: bool
    postmortem_notified_twitter: bool
    postmortem_published_at: None
    resolved_at: None
    scheduled_auto_transition: bool
    scheduled_for: None
    scheduled_remind_prior: bool
    scheduled_reminded_at: None
    scheduled_until: None
    shortlink: str
    status: str
    updated_at: datetime
    id: str
    organization_id: str
    incident_updates: List[IncidentUpdate]
    name: str

    def __init__(self, backfilled: bool, created_at: datetime, impact: str, impact_override: None, monitoring_at: datetime, postmortem_body: None, postmortem_body_last_updated_at: None, postmortem_ignored: bool, postmortem_notified_subscribers: bool, postmortem_notified_twitter: bool, postmortem_published_at: None, resolved_at: None, scheduled_auto_transition: bool, scheduled_for: None, scheduled_remind_prior: bool, scheduled_reminded_at: None, scheduled_until: None, shortlink: str, status: str, updated_at: datetime, id: str, organization_id: str, incident_updates: List[IncidentUpdate], name: str) -> None:
        self.backfilled = backfilled
        self.created_at = created_at
        self.impact = impact
        self.impact_override = impact_override
        self.monitoring_at = monitoring_at
        self.postmortem_body = postmortem_body
        self.postmortem_body_last_updated_at = postmortem_body_last_updated_at
        self.postmortem_ignored = postmortem_ignored
        self.postmortem_notified_subscribers = postmortem_notified_subscribers
        self.postmortem_notified_twitter = postmortem_notified_twitter
        self.postmortem_published_at = postmortem_published_at
        self.resolved_at = resolved_at
        self.scheduled_auto_transition = scheduled_auto_transition
        self.scheduled_for = scheduled_for
        self.scheduled_remind_prior = scheduled_remind_prior
        self.scheduled_reminded_at = scheduled_reminded_at
        self.scheduled_until = scheduled_until
        self.shortlink = shortlink
        self.status = status
        self.updated_at = updated_at
        self.id = id
        self.organization_id = organization_id
        self.incident_updates = incident_updates
        self.name = name
