# Сайт про события на карте
На карте размещаются метки событий, по клику на метке можно узнать информацию и увидеть фотографии. [Пример сайта](http://zedchi.pythonanywhere.com/) и [его административная панель](http://zedchi.pythonanywhere.com/admin). Данные берутся с "Яндекс.Афиши" или подобных сайтов.

## Требования:
- python 3.7
- установленный pipenv, [инструкция по установке](https://pipenv.pypa.io/en/latest/install/#installing-pipenv).

## Установка:
- клонировать репозиторий к себе на компьютер.
- в папке проекта из консоли набрать `pipenv install`, дождаться установки.
- в папке afisha создать файл .env и прописать значения (но не обязательно):
    ```
    DEBUG=<True или False>
    SECRET_KEY=<уникальный набор символов>
    ``` 
    - DEBUG - переменная вкл/выкл режима отладки. По умолчанию выкл.
    - SECRET_KEY - уникальный код вашего приложения, используется для криптографических процедур.
- запуск скриптов .py должен производиться из оболочки pipenv: `pipenv shell`.
- для доступа к административной панели требуется создать пользователя командой: `python manage.py createsuperuser`.

## Наполнение базы:
- из административной панели
- либо командой `python manage.py load_place <адрес json файла>`
- структура json файл должна быть такого типа:
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
Команда `python manage.py runserver`.

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
