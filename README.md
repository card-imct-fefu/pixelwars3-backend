![Logo](.github/assets/logo.png)
-----

Серверная часть [Pixel Wars 3](https://fefuwars3.herokuapp.com/).

# Быстрый старт

Склонируйте проект
```bash
git clone https://github.com/card-imct-fefu/pixelwars3-backend.git
cd pixelwars3-backend
```

Создайте файлы ``.env`` и ``.env.dev`` в корне проекта и установите переменные
среды:
```bash
touch .env
echo APP_ENV=dev > .env

touch .env.dev
echo DATABASE_URL=DATABASE_URL > .env.dev
echo APP_CLIENT_ID=APP_CLIENT_ID > .env.dev
echo TENANT_ID=TENANT_ID > .env.dev
echo OPENAPI_CLIENT_ID=OPENAPI_CLIENT_ID > .env.dev
echo SECRET_KEY=$(openssl rand -hex 32) > .env.dev
```
Для запуска необходимо выполнить команды:
```bash
docker-compose build
docker-compose up -d
```

# Подготовка среды для разработки
Выполните следующие команды, чтобы загрузить вашу среду с ``poetry``: 
```bash
poetry install
poetry shell
```

# Makefile
 - ``make lint`` - flake8, black (check)
 - ``make pretty`` - isort, black
 - ``make init_db`` - применение миграций
 - ``make run`` - запуск сервера через uvicorn

# Запуск тестов
TODO

# Документация
Документация доступна по ручкам ``/docs`` или ``/redoc`` с помощью
Swagger или ReDoc соотвественно.
