FROM python:3.12-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG NODE_MAJOR=18

# Set work directory
WORKDIR /app

# Install dependencies
RUN pip install poetry
COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-dev

# Copy project
COPY . /app/

# Run migrations
RUN poetry run python manage.py makemigrations
RUN poetry run python manage.py migrate

# Expose port
EXPOSE 8000
# Command to run the server
CMD ["poetry", "run", "python", "manage.py", "tailwind", "runserver", "0.0.0.0:8000"]

