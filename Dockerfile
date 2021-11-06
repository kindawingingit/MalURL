FROM python:3.9.5

WORKDIR /app

COPY . .

RUN ["pip3", "install", "pipenv"]

RUN ["pip3", "install", "--upgrade", "pip"]

RUN ["pipenv", "install"]

RUN ["pipenv", "install", "xgboost"]

ENV FLASK_APP web/app

ENV PYTHONPATH "${PYTHONATH}:/app/web:/app/models"

CMD ["pipenv","run", "flask", "run", "--host=0.0.0.0"]
