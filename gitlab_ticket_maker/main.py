import os

import click
import click_completion

from gitlab_ticket_maker.constant.default_options import DEFAULT_PRIORITY, DEFAULT_SEVERITY, DEFAULT_SCOPE, \
    DEFAULT_SQUAD, DEFAULT_PROJECT_ID, DEFAULT_SERVER_URL
from gitlab_ticket_maker.description import get_description

click_completion.init()


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
              default=lambda: os.getenv(DEFAULT_PRIORITY, 1),
              show_default=f"Content of ${DEFAULT_PRIORITY}",
              )
@click.option('--severity',
              type=click.IntRange(1, 4),
              prompt=True,
              default=lambda: os.getenv(DEFAULT_SEVERITY, 1),
              show_default=f"Content of ${DEFAULT_SEVERITY}",
              )
@click.option('--scope',
              type=click.STRING,
              prompt=True,
              default=lambda: os.getenv(DEFAULT_SCOPE, ""),
              show_default=f"Content of ${DEFAULT_SCOPE}",
              )
@click.option('--squad',
              type=click.STRING,
              prompt=True,
              default=lambda: os.getenv(DEFAULT_SQUAD, ""),
              show_default=f"Content of ${DEFAULT_SQUAD}",
              )
@click.option('--project-id',
              type=click.INT,
              envvar=DEFAULT_PROJECT_ID,
              show_default=f"Content of ${DEFAULT_PROJECT_ID}",
              )
@click.option('--server-url',
              type=click.STRING,
              envvar=DEFAULT_SERVER_URL,

              show_default=f"Content of ${DEFAULT_SERVER_URL}",
              )
def new(title: str,
        skip_description: bool,
        priority: int,
        severity: int,
        scope: str,
        squad: str,
        project_id: int,
        server_url: str):
    print(title, skip_description, priority, severity, scope, squad, project_id, server_url)
    description = get_description(skip_description)
    click.echo(f"Description:\n{description}")


if __name__ == '__main__':
    cli()
