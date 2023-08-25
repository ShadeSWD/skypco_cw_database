# Приложение для сбора вакансий с hh.ru

Приложение предназначено для сбора вакансий интересующих работодателей и навигации в собранных данных

## Установка и настройка окружения

1. Клонируйте репозиторий с приложением:

```shell
   git clone https://github.com/ShadeSWD/skypco_cw_database
```

2. Установите необходимые зависимости с помощью poetry:

3. Создайте базу данных PostgreSQL с именем vacancies
4. Создайте переменную среды "pgAdmin", значение которой будет пароль от pgAdmin.

## Запуск приложения

Запустите главный файл приложения main.py:

```shell
   python main.py
```

## Функциональность приложения

Приложение предоставляет следующую функциональность:

1. Получение списка всех компаний и количества вакансий у каждой компании.
2. Получение списка всех вакансий, у которых зарплата выше средней по всем вакансиям.
3. Получение списка всех вакансий, в названии которых содержится заданное ключевое слово.