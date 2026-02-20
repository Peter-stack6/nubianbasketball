FROM python:3.11-slim

WORKDIR / app

COPY requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONBUFFERED=1

EXPOSE 10000

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:10000"]
