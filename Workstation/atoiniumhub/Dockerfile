
FROM python:3.9-slim


RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=atoiniumhub.settings


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]