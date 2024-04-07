# OtakuSearch
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![Django Version](https://img.shields.io/badge/django-5.0.2-green)](https://www.djangoproject.com/)
[![Poetry Version](https://img.shields.io/badge/poetry-1.8.2%2B-brightgreen)](https://python-poetry.org/)
[![Tailwind Version](https://img.shields.io/badge/django--tailwind--cli-1.3.1-orange)](https://github.com/oliverandrich/django-tailwind-cli)

[![Demo Website](https://img.shields.io/badge/demo-website-gree)](https://otaku.smuks.org/)

Django project to learn how it works.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
  - [Docker](#docker)
  - [Locally](#locally)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Docker
- Python 3.12 (To run locally)
- Poetry (To run locally)

## Installation

### Docker

1. Clone the repository:

    ```bash
    git clone https://github.com/Arnaldopower/OtakuSearch.git
    ```

2. Navigate to the project directory:

    ```bash
    cd OtakuSearch
    ```

3. Build and run the Docker container:

    ```bash
    docker-compose up --build
    ```

4. Access the application at `http://localhost:8000`.

### Locally
1. Clone the repository:

    ```bash
    git clone https://github.com/Arnaldopower/OtakuSearch.git
    ```

2. Navigate to the project directory:

    ```bash
    cd OtakuSearch
    ```
3. Run Django with tailwind-cli
   ```bash
   poetry run python manage.py tailwind start
   ```

4. Access the application at `http://localhost:8000`.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature`)
3. Make changes and commit (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature`)
5. Create a pull request

## License

[MIT License](LICENSE)
