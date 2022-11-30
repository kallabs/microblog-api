FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /prj

COPY ./requirements.txt .
COPY ./alembic.ini .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./alembic .
COPY ./src/microblog .

CMD ["uvicorn", "microblog.main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
