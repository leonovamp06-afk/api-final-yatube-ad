# API для Yatube

Социальная сеть с API на Django REST Framework.

## Установка

1. Клонируйте репозиторий
2. Создайте виртуальное окружение: `python -m venv venv`
3. Активируйте окружение: `source venv/Scripts/activate`
4. Установите зависимости: `pip install -r requirements.txt`
5. Выполните миграции: `python manage.py migrate`
6. Запустите сервер: `python manage.py runserver`

## Документация

После запуска документация доступна по адресу: http://127.0.0.1:8000/redoc/

## Примеры запросов

### Получение JWT-токена

POST /api/v1/jwt/create/

{
    "username": "your_username",
    "password": "your_password"
}

### Создание поста

POST /api/v1/posts/
Authorization: Bearer <ваш_токен>

{
    "text": "Мой первый пост",
    "group": 1
}

### Подписка

POST /api/v1/follow/
Authorization: Bearer <ваш_токен>

{
    "following": "username"
}
