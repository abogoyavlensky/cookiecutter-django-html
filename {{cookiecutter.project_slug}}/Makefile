COMPOSE = docker-compose
GOALS = $(filter-out $@,$(MAKECMDGOALS))
BASE_APP = app

YELLOW := "\e[1;33m"
NC := "\e[0m"
INFO := @sh -c '\
    printf $(YELLOW); \
    echo "=> $$1"; \
    printf $(NC)' VALUE

PEP8_CLEANED ?= {{cookiecutter.project_slug}}

.SILENT: # Ignore output of make `echo` command


.PHONY: help # [Local] Generate list of targets with descriptions
help:
	@grep '^.PHONY: .* #' Makefile | sed 's/\.PHONY: \(.*\) # \(.*\)/\1 > \2/' | column -tx -s ">"


.PHONY: lint # [Local] Run linting of py-files
lint:
	@$(INFO) "Running flake8..."
	@flake8 --statistics --config=setup.cfg $(PEP8_CLEANED)
	@$(INFO) "Running pylint..."
	@pylint -j 4 $(PEP8_CLEANED)


.PHONY: fmt # [Local] Format code
fmt:
	@$(INFO) "Formatting imports..."
	@isort $(PEP8_CLEANED)
	@$(INFO) "Formatting code..."
	@black $(PEP8_CLEANED)


.PHONY: fmt-check # [Local] Jsut check code formatting
fmt-check:
	@$(INFO) "Formatting imports..."
	@isort $(PEP8_CLEANED) --diff
	@$(INFO) "Formatting code..."
	@black $(PEP8_CLEANED) --diff


.PHONY: clean # [Local] Clean temp files from projects: .pyc. .pyo, __pycache__
clean:
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete
	@rm -rf .pytest_cache .mypy_cache


.PHONY: up # [Local] Run all docker compose deps
up:
	@$(COMPOSE) up -d


.PHONY: manage # [Docker] Run any django command
manage:
	@$(COMPOSE) run $(BASE_APP) python manage.py $(GOALS)


.PHONY: run # [Docker] Run any command inside run container
run:
	@$(COMPOSE) run $(BASE_APP) $(GOALS)


.PHONY: test # [Docker] Run test with forcing creting db. Example: `make test`
test:
	@$(COMPOSE) run $(BASE_APP) pytest --create-db

