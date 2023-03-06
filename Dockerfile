FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/prj/src"

WORKDIR /prj

COPY ./requirements.txt .
COPY ./alembic.ini .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./alembic .
COPY ./tests .
COPY ./src .

WORKDIR /prj/src

CMD ["uvicorn", "microblog.entrypoints.app:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
