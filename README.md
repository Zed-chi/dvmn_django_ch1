# Сайт про события на карте

Данные берутся с  "Яндекс.Афиши"  или подобных сайтов

[Пример сайта](http://zedchi.pythonanywhere.com/)

[Административная часть сайта](http://zedchi.pythonanywhere.com/admin)

## Требования:
- python 3.7
- устанавленный pipenv, [инструкция по установке](https://pipenv.pypa.io/en/latest/install/#installing-pipenv)

## Установка:
- Склонировать репозиторий к себе
- В папке проекта из консоли набрать `pipenv install`, дождаться установки
- в папке afisha создать файл .env и прописать значения:
    ```
    DEBUG=<True или False>
    SECRET_KEY=<уникальный набор символов>
    ```
- запуск скриптов .py должен производиться из оболочки pipenv: `pipenv shell`
- для доступа к административной панели требуется создать пользователя: `python manage.py createsuperuser`

## Наполнение базы:
- из администартивной панели
- либо командой `python manage.py load_place <адрес json файла>`
json файл типа:
    ```json
    {
    	"title": <НАЗВАНИЕ>,
    	"imgs": [ <ССЫЛКИ  НА  ФОТО  ЧЕРЕЗ  ЗАПЯТУЮ>],
    	"description_short": <КОРОТКОЕ  ОПИСАНИЕ>,
    	"description_long": <ДЛИННОЕ  ОПИСАНИЕ>,
    	"coordinates": {
    		"lng": <ДОЛГОТА>,
    		"lat": <ШИРОТА>
    	}
    }
    ```

## Запуск:
Команда `python manage.py runserver`

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/)
