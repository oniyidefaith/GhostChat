FROM python:3.8-slim


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*


COPY requirements.txt /app/
RUN pip install --upgrade pip && \
  pip install --no-cache-dir -r requirements.txt

COPY . /app/


EXPOSE 8000


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "anon.wsgi:application"]
