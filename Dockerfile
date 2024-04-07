FROM python:3.12-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG NODE_MAJOR=18

# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update \
  && apt-get install -y ca-certificates curl gnupg \
  && mkdir -p /etc/apt/keyrings \
  && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
  && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list \
  && apt-get update \
  && apt-get install nodejs -y \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean

RUN pip install poetry
COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-dev

# Copy project
COPY . /app/

# Run migrations
RUN poetry run python manage.py makemigrations
RUN poetry run python manage.py migrate
RUN poetry run python manage.py tailwind install --no-input;
RUN poetry run python manage.py tailwind build --no-input;
RUN poetry run python manage.py collectstatic --no-input;
# Expose port
EXPOSE 8000
# Command to run the server
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

