FROM python:3.11.2
RUN apt-get update && apt install -y curl
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="${PATH}:/root/.local/bin"
RUN poetry config virtualenvs.in-project true
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install
COPY . .
