FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PLAYWRIGHT_BROWSERS_PATH=/app/ms-playwright

COPY Pipfile.lock Pipfile ./
RUN pip install -U pip setuptools pipenv && pipenv install

COPY . .

RUN pipenv run python3 -m playwright install chromium
RUN pipenv run python3 -m playwright install-deps

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
