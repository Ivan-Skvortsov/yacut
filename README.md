<div id="top"></div>
<div align="center">
<h1>Проект YaCut</h1>
  <h3>
    Сервис укорачивания ссылок.
    <br />
  </h3>
</div>

## О проекте
 Назначение сервиса — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис. Например, ссылка `https://www.google.ru/maps/@55.7941639,49.1372337,11.92z` может быть представлена в виде `http://yacut.ru/KazanMap`.<br />
Ключевые возможности сервиса:
- генерация коротких ссылок и связь их с исходными длинными ссылками
- переадресация на исходный адрес при обращении к коротким ссылкам
- реализованный API

<p align="right">(<a href="#top">наверх</a>)</p>

## Использованные технологии и пакеты
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [WTForms](https://wtforms.readthedocs.io/en/3.0.x/)

<p align="right">(<a href="#top">наверх</a>)</p>

## Необходимый софт
Для развертывания проекта локально, на Вашем комьютере требуется Python вресии 3.8.10 и выше. <br>
Скачать дистрибутив для Вашей ОС можно на официальном сайте: https://www.python.org/downloads/

## Установка
Склонируйте проект на Ваш компьютер
   ```sh
   git clone https://github.com/Ivan-Skvortsov/yacut.git
   ```
Перейдите в папку с проектом
   ```sh
   cd yacut
   ```
Активируйте виртуальное окружение
   ```sh
   python3 -m venv venv
   ```
   ```sh
   source venv/bin/activate
   ```
Обновите менеджер пакетов (pip)
   ```sh
   pip3 install --upgrade pip
   ```
Установите необходимые зависимости
   ```sh
   pip3 install -r requirements.txt
   ```
<p align="right">(<a href="#top">наверх</a>)</p>

<!-- ## Тестовые базы данных
В репозитории, в директории /api_yamdb/static/data, подготовлены несколько файлов в формате csv с контентом для ресурсов Users, Titles, Categories, Genres, Review и Comments. Вы можете заполнить базу данных контентом из приложенных csv-файлов. Для этого необходимо выполнить команду:
   ```sh
   python3 manage.py import_csv
   ```
<p align="right">(<a href="#top">наверх</a>)</p> -->

## Использование
Для запуска проекта выполните команду
```sh
flask run
```
### Пользовательский интерфейс
Пользовательский интерфейс сервиса — одна страница с формой из двух полей:
- исходная ссылка (обязательное поле)
- пользовательская ссылка (необязательное поле)
Пользовательский вариант короткой ссылки не должен превышать 16 символов.
Если пользователь не заполнит поле со своим вариантом короткой ссылки, то сервис генерирует её автоматически.

### API проекта
Cервис обслуживает два эндпоинта:
 - `/api/id/` — POST-запрос на создание новой короткой ссылки;
 - `/api/id/<short_id>/` — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.
<p align="right">(<a href="#top">наверх</a>)</p>

## Об авторе
Автор проекта: Иван Скворцов<br/><br />
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ivan-Skvortsov/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:pprofcheg@gmail.com)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Profcheg)
<p align="right">(<a href="#top">наверх</a>)</p>