FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir /code/static

COPY wait-for-db.sh /code/wait-for-db.sh

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]