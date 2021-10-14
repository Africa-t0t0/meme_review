FROM python:3.8.3-slim
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
COPY requirements.txt /tmp/
WORKDIR /app
COPY backend.py /app/.
COPY /memes/ /app/memes 
RUN pip install --upgrade pip
RUN pip install --requirement /tmp/requirements.txt
CMD ["python3","/app/backend.py"]


