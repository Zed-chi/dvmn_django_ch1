# Сайт про события на карте
Данный берутся с Яндекс.Афиши или подобных сайтов

[Пример сайта](http://zedchi.pythonanywhere.com/)

[Административная часть сайта](http://zedchi.pythonanywhere.com/admin)

## Требования:
- python 3.7
- устанавленный pipenv [инструкция](https://pipenv.pypa.io/en/latest/install/#installing-pipenv)

## Установка:
* Склонировать репозиторий к себе
* В папке проекта из консоли набрать `>> pipenv install `, дождаться установки
* в папке afisha создать файл .env и прописать значения:
```
DEBUG=<True или False>
SECRET_KEY=<уникальный набор символов>
```
* запуск скриптов .py должен производиться из оболочки pipenv - `pipenv shell`

для доступа к административной панели требуется создать пользователя:
`python manage.py createsuperuser`

## Запуск:
```
>> `python manage.py runserver`
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/)
