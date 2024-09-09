КАК РАЗВЕРНУТЬ ПРИЛОЖЕНИЕ DJANGO
1) создаем директорию проекта
2) создание файла requirements.txt
    2.1) djangorestframework, psycopg2-binary, python-decouple
3) создание виртуального окружения 
    3.1) python3 -m venv venv
4) pip install -r requirements.txt - скачиваем все зависимости

КОМАНДЫ:
1) django-admin startproject config . - создает проект,  если поставить . то проект создается в этой же директории, если не поставить, то создастся папка config, и в ней создастся проект

2) ./manage.py startapp <app_name> - создает приложение
3) ./manage.py makemigrations - проверяет все файлы models.py, если есть изменения, то создается новый файл в папке migrations с изменениями
4) ./manage.py migrate - проводит все зафиксированные миграции, и добавляет все изменения в бд (создание таблиц/изменения таблиц/удаление таблиц и тд.)
5) ./manage.py runserver - запускает наш проект на 127.0.0.1:8000 (localhost:8000)
    5.1) ./manage.py runserver 5000

