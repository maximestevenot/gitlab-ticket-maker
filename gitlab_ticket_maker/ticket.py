import os

from gitlab import Gitlab
from gitlab.v4.objects import Project

from gitlab_ticket_maker.constant.gitlab import GITLAB_SERVER_URL, GITLAB_API_TOKEN, PRIORITY_PREFIX, SEVERITY_PREFIX, \
    SCOPE_PREFIX, SQUAD_PREFIX, TITLE, DESCRIPTION, LABELS, TicketType, TYPE_PREFIX


def get_labels(priority: int, severity: int, type: TicketType, scope: str, squad: str) -> list[str]:
    labels = [PRIORITY_PREFIX + str(priority),
              TYPE_PREFIX + type.name.lower(),
              SCOPE_PREFIX + scope,
              SQUAD_PREFIX + squad]

    if type in [TicketType.BUG, TicketType.INCIDENT, TicketType.REQUEST, TicketType.SUPPORT]:
        labels.append(SEVERITY_PREFIX + str(severity))

    return labels


class GitlabConfigException(Exception):
    pass


def no_gitlab_config_error(parameter: str):
    raise GitlabConfigException(f"{parameter} not defined")


def get_config() -> tuple[str, str]:
    server_url = os.getenv(GITLAB_SERVER_URL) or no_gitlab_config_error(GITLAB_SERVER_URL)
    api_token = os.getenv(GITLAB_API_TOKEN) or no_gitlab_config_error(GITLAB_API_TOKEN)
    return server_url, api_token


def get_project(project_id: int) -> Project:
    server_url, api_token = get_config()
    instance: Gitlab = Gitlab(server_url, private_token=api_token)
    return instance.projects.get(project_id, lazy=True)


def create_issue(project_id: int, issue_content: dict) -> str:
    project = get_project(project_id)
    issue = project.issues.create({TITLE: issue_content[TITLE],
                                   DESCRIPTION: issue_content[DESCRIPTION],
                                   LABELS: issue_content[LABELS]})
    return issue.attributes["web_url"]
