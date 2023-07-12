# SHIFT project FastAPI

## Список примененных технологий:
```
python==3.10
alembic==1.11.1
fastapi==0.98.0
psycopg2==2.9.6
pydantic==1.10.9
PyJWT==2.7.0
python-dotenv==1.0.0
SQLAlchemy==2.0.17
uvicorn==0.22.0
```

## Как запустить проект локально:
Клонировать репозиторий:

```
git clone git@github.com:EvgenyF90/SHIFT_project_FastAPI.git
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source env/bin/activate - iOS
source venv/scripts/activate - Windows
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Наполненить env-файл:
```
DB_ENGINE=указываем базу данных
DB_NAME=имя базы данных
POSTGRES_USER=логин для подключения к базе данных
POSTGRES_PASSWORD=пароль для подключения к БД
DB_HOST=localhost
DB_PORT=порт для подключения к БД
JWT_SECRET_KEY=секретный ключ для подключения JWT-токена
```

Выполнить миграции и наполнить базу данными:

```
alembic revision --autogenerate -m 'BD creation'
alembic upgrade head
```

Запустить проект:

```
uvicorn main:app --reload
```

Список запросов к API можно посмотреть по адресу:

```
http://127.0.0.1:8000/docs/
```

## Запуск через Docker:
```
docker-compose up -d --build
```
Docker образ: evgenyf90/shift_project:latest


## Автор
https://github.com/EvgenyF90/
