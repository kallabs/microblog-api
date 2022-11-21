FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /prj/src
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . ./
EXPOSE 8000