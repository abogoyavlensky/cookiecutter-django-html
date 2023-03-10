# {{cookiecutter.project_name}}

## Requirements

* Python >= 3.11.1
* Django >= 4.1.7

## Local developemnt

Create `.env` at the root of project dir with content similar to `.env.example`.

*`.env` Must not be commited to git repository!*

Before you start please install docker and docker-compose on the host.
Then you could perfom serveral command using `make`:

```bash
make help     
help         [Local] Generate list of targets with descriptions
lint         [Local] Run linting of py-files
fmt          [Local] Format code
fmt-check    [Local] Jsut check code formatting
clean        [Local] Clean temp files from projects: .pyc. .pyo, __pycache__
up           [Local] Run all docker compose deps
manage       [Docker] Run any django command
run          [Docker] Run any command inside run container
test         [Docker] Run test with forcing creting db. Example: `make test`
```

After runnint `make up` command you could see a running web application at `http://localhost:8000/`.

## Install git-hook on pre-commit

You could install preconfigured git hooks using [lefthook](https://github.com/evilmartians/lefthook):

```bash
$ lefthook install
```
