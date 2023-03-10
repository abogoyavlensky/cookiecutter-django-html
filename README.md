Django HTML boilerplate
===

## Requirements

* Python >= 3.11.1
* Django >= 4.1.7

## Features

- `Docker Compose` local setup with minimal `docker`-image
- Convenient `make`-commands to manage the project
- Testing with `py.test` and `django-dynamic-fixture`
- Checking lint and auto formatting

## Installation

First of all, you need to install `cookiecutter` python package. And then
just run it pointed to the repository:

```bash
$ pip install cookiecutter
$ cookiecutter gh:abogoyavlensky/cookiecutter-django-html
```

Now, your project has been configured and ready for further development:

```bash
$ cd <project_name>
$ make help
$ make up
$ make manage createsuperuser
```

## Inspired by

- https://github.com/pydanny/cookiecutter-django
- https://github.com/feldroy/django-crash-starter
- https://github.com/wemake-services/wemake-django-template


# TODO:

- [ ] django-debug-toolbar
- [ ] mypy
- [ ] check code complexity (xenon)
