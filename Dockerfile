FROM python:3.10

WORKDIR /code

COPY pyproject.toml /code

RUN pip install poetry

RUN poetry install

COPY . /code

CMD ["poetry", "run", "uvicorn", "weather_app.main:app", "--host", "0.0.0.0", "--port", "8080"]

