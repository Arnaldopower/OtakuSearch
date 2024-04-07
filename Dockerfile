FROM python:3.12-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG NODE_MAJOR=18

# Set work directory
WORKDIR /app

# Install dependencies
RUN curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/download/v3.4.3/tailwindcss-linux-x64
RUN chmod +x tailwindcss-linux-x64
RUN mv tailwindcss-linux-x64 tailwindcss
RUN ./tailwindcss init
RUN
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
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

