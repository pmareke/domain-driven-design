FROM python:3.10

WORKDIR /code

COPY pyproject.toml /code

RUN pip install poetry

RUN poetry install

COPY . /code

EXPOSE 8080

CMD ["poetry", "run", "fastapi", "run", "weather_app/main.py", "--port", "8080"]

