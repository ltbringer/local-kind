FROM rayproject/ray:2.20.0.0ae93f-py310

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root

COPY project /app/project
COPY artifacts /app/artifacts

RUN poetry install
