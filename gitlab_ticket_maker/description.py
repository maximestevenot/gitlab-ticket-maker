import click

MARKER = "[//]: # (Everything below is ignored.)"


def build_prompt() -> str:
    help_message = "[//]: # (Please fill the issue description.)\n[//]: # (Markdown format is supported.)"
    return f"\n\n{MARKER}\n{help_message}\n"


def get_description_from_prompt() -> str:
    message = click.edit(build_prompt(), extension=".md")
    return message.split(MARKER, 1)[0].rstrip('\n') if message else ""


def get_description(skip_prompt: bool) -> str:
    footer = "*This issue has been created thanks " \
             "[Gitlab Ticket Maker](https://github.com/maximestevenot/gitlab-ticket-maker.git)*"
    body = get_description_from_prompt() if not skip_prompt else ""
    return f"{body}\n\n{footer}"
