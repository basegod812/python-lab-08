FROM python:3.12-slim
WORKDIR /app
RUN python -m pip install --no-cache-dir "poetry>=2.1,<3"
COPY pyproject.toml README.md ./
RUN poetry config virtualenvs.create false && poetry lock && poetry install --no-root --only main
COPY src/ ./src/
ENV PYTHONPATH=/app/src
CMD ["python", "-m", "calculator"]
