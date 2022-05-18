# Ticket Maker

A simple command line tool to create new Gitlab Issues

:warning: This first version is closely coupled with Sopra Banking Cloud Platform flow.

## Gitlab Configuration

The following environment variables are needed:

- `GITLAB_SERVER_URL`: The URL of the Gitlab server where your project is located.
- `GITLAB_API_TOKEN`: Your Gitlab token with API Write scope for the project where you want to create issue.

## Default Parameters

Tickets information can have default configuration via environment variables.

| Variable             | Example Value            |
|----------------------|--------------------------|
| TKT_DEFAULT_PRIORITY | 1                        |
| TKT_DEFAULT_SEVERITY | 1                        |
| TKT_DEFAULT_TYPE     | bug                      |
| TKT_DEFAULT_SCOPE    | "saas-runtime"           |
| TKT_DEFAULT_SQUAD    | "saas-runtime-taskforce" |
| TKT_PROJECT_ID       | 73237                    |

## Usage

```bash
$ tkt new --help
Usage: main.py new [OPTIONS]

Options:
  -t, --title TEXT          Issue Title
  --skip-description        Skip editor prompt to add a description  [default:
                            False]
  --priority INTEGER RANGE  [default: (Content of
                            $TKT_DEFAULT_PRIORITY);1<=x<=4]
  --severity INTEGER RANGE  [default: (Content of
                            $TKT_DEFAULT_SEVERITY);1<=x<=4]
  --scope TEXT              [default: (Content of $TKT_DEFAULT_SCOPE)]
  --squad TEXT              [default: (Content of $TKT_DEFAULT_SQUAD)]
  --project-id INTEGER      [default: (Content of $TKT_PROJECT_ID)]
  --help                    Show this message and exit.
```


