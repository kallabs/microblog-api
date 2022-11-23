FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /prj

COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]