FROM python:3.11.2-slim-buster

# Setup env vars
ENV POETRY_VERSION=1.3.2 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIPENV_COLORBLIND=true

# Install deps
RUN apt-get update && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
    bash \
    netcat \
    build-essential \
    gettext \
    libpq-dev \
    make \
    curl \
    git \
  && curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.4.0 python3 - \
  && poetry --version \
  # Cleaning cache:
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# User 
RUN addgroup --system web \
    && adduser --system --ingroup web web

# Copy only requirements, to cache them in docker layer
COPY ./poetry.lock ./pyproject.toml /app/

# Install deps
RUN poetry install --no-interaction --no-ansi

# Scripts
COPY --chown=web:web ./scripts/wait-for.sh /wait-for.sh
RUN chmod +x /wait-for.sh

COPY --chown=web:web ./scripts/gunicorn.sh /gunicorn.sh
RUN chmod +x /gunicorn.sh

RUN chown web:web /app

USER web
