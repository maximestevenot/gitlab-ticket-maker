import os

import click
import click_completion

from gitlab_ticket_maker.constant.default_options import DEFAULT_PRIORITY, DEFAULT_SEVERITY, DEFAULT_SCOPE, \
    DEFAULT_SQUAD, DEFAULT_PROJECT_ID, DEFAULT_TYPE
from gitlab_ticket_maker.constant.gitlab import TITLE, DESCRIPTION, LABELS, TicketType
from gitlab_ticket_maker.description import get_description
from gitlab_ticket_maker.ticket import create_issue, get_labels

click_completion.init()

TICKET_TYPES = click.Choice([f.value for f in TicketType], case_sensitive=False)


@click.group()
def cli():
    pass


@cli.command("new", short_help="Open a new issue")
@click.option("-t", "--title",
              help="Issue Title",
              type=click.STRING,
              prompt=True,
              )
@click.option('--skip-description',
              help='Skip editor prompt to add a description',
              is_flag=True,
              default=False,
              show_default=True,
              )
@click.option('--priority',
              type=click.IntRange(1, 4),
              prompt=True,
              default=lambda: os.getenv(DEFAULT_PRIORITY),
              show_default=f"Content of ${DEFAULT_PRIORITY}",
              )
@click.option('--severity',
              type=click.IntRange(1, 4),
              prompt=True,
              default=lambda: os.getenv(DEFAULT_SEVERITY),
              show_default=f"Content of ${DEFAULT_SEVERITY}",
              )
@click.option('--type',
              type=TICKET_TYPES,
              prompt=True,
              default=lambda: os.getenv(DEFAULT_TYPE),
              show_default=f"Content of ${DEFAULT_TYPE}",
              )
@click.option('--scope',
              type=click.STRING,
              prompt=True,
              default=lambda: os.getenv(DEFAULT_SCOPE),
              show_default=f"Content of ${DEFAULT_SCOPE}",
              )
@click.option('--squad',
              type=click.STRING,
              prompt=True,
              default=lambda: os.getenv(DEFAULT_SQUAD),
              show_default=f"Content of ${DEFAULT_SQUAD}",
              )
@click.option('--project-id',
              type=click.INT,
              envvar=DEFAULT_PROJECT_ID,
              show_default=f"Content of ${DEFAULT_PROJECT_ID}",
              )
def new(title: str,
        skip_description: bool,
        priority: int,
        severity: int,
        type: str,
        scope: str,
        squad: str,
        project_id: int):
    description = get_description(skip_description)

    issue_url = create_issue(project_id, {
        TITLE: title,
        DESCRIPTION: description,
        LABELS: get_labels(priority, severity, TicketType[type.upper()], scope, squad)
    })

    click.secho(f"Issue created at {issue_url}", fg='green')


if __name__ == '__main__':
    cli()
