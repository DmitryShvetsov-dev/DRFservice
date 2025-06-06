# DjangoRestframework Service

**DRFservice** пример проекта с использованием Django + PostgreSQL + psycopg2, Django REST framework,SQLAlchemy + psycopg2, pyTelegramBotAPI
## Установка
1. Склонируйте репозиторий 
```bash
git clone https://github.com/DmitryShvetsov-dev/DRFservice.git
```
2. В корне проекта создайте файл .env и разместите там следующие переменные окружения:
- DJANGO_SECRET_KEY =
- DATABASE_NAME=
- DATABASE_USERNAME=
- DATABASE_PASSWORD=
- DATABASE_PORT=
- DATABASE_HOST=
- TELEGRAM_TOKEN=
- DATABASE_URL=
```
│
├── DRFapp
├── .env           # Файл должен распологаться тут
├── .gitignore
└── docker-compose.yml
```
3. Убедитесь что у вас установлен docker, затем выполните команду в директории проекта:
```bash
docker-compose up --build
```
4. По завершению установки для корректной работы требуется создать миграции, так же создадим сразу суперпользователя для админки
 - не закрывая прошлый терминал, откройте второй терминал в той же директории и выполните следующие команды
```bash
docker-compose exec web-app python manage.py makemigrations
```
```bash
docker-compose exec web-app python manage.py migrate
```
```bash
docker-compose exec web-app python manage.py createsuperuser
```
