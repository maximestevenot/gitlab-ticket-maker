from enum import Enum

GITLAB_SERVER_URL = "GITLAB_SERVER_URL"
GITLAB_API_TOKEN = "GITLAB_API_TOKEN"

TYPE_PREFIX = "type::"
SCOPE_PREFIX = "scope::"
PRIORITY_PREFIX = "priority::P"
SEVERITY_PREFIX = "severity::S"
SQUAD_PREFIX = "squad:"
TYPE_PREFIX = "type::"

TITLE = "title"
DESCRIPTION = "description"
LABELS = "labels"


class TicketType(Enum):
    BUG = "bug"
    FEATURE = "feature"
    IMPROVEMENT = "improvement"
    INCIDENT = "incident"
    REQUEST = "request"
    SUPPORT = "support"
