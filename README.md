# Message Server Bot

## Задача

**Написать docker compose, в котором работают:**

- Web приложение, на FastApi. У приложения должно быть несколько ендпоинтов:

  - GET 'api/v1/messages/' показывает список всех сообщений;

  - POST 'api/v1/message/' позволяет написать сообщение.

- Веб сервер должен быть Nginx.

- Mongo как БД для сообщений.

- Телеграм бот (aiogram3), который показывает сообщения и позволяет создать сообщение самому.

**Будет плюсом:**

  1) Добавление кэширования при помощи Redis (кеш стирается, когда появляется новое сообщение)

  2) Развертывание на удалённом сервере и добавление ssl через certbot.

  3) Реализовать код так, чтобы было видно, кто написал сообщение.
  
  4) Добавление пагинации.

## Результат

**Docker compose, в котором работают:**

- Web приложение, на FastApi. У приложения должно быть несколько ендпоинтов:

  - GET 'api/v1/messages/' показывает список всех сообщений;

  - POST 'api/v1/message/' позволяет написать сообщение.

- Веб сервер Nginx.

- MongoDB как БД для сообщений.

- Телеграм бот (aiogram3), который показывает сообщения и позволяет создать сообщение самому.

- Кэширование при помощи Redis (кеш стирается, когда появляется новое сообщение).

- Код реализован так, что видно, кто написал сообщение.

- Я не стал делать развертывание на удаленном сервере и ssl, так как слабо разбираюсь в этом пункте.

## Описание проекта

### Структура проекта

**Проект построен следующим образом:**

![image](https://github.com/user-attachments/assets/aae79f4b-5fa4-4060-9712-9bde5e2761b0)

#### Файлы кода

**В папке app находится код API на FastAPI:**

  - _routers/messages.py:_ Маршрутизатор сообщений.

  - _config.py:_ Параметры приложения (Извлечение данных из .env).

  - _database.py:_ Взаимодейтсвие с MongoDB.

  - _models.py:_ Модели Pydantic для валидации.

  - _main.py:_ Точка входа для API.

**В папке bot находится код Telegram-Бота на Aiogram3:**

  - _handlers.py:_ Маршрутизатор сообщений с обработчиками.

  - _config.py:_ Параметры бота (Извлечение данных из .env).

  - _main.py:_ Точка входа для Бота.

#### Оставшиеся файлы

В корне проекта:

  - _.env:_ Файл с настройками для всего приложения (Не экспортируется на GitHub в целях безопасности).

  - _.gitignore:_ Файл с указанием игнорирования папок и файлов для системы контроля версий Git.

  - _docker-compose.yml:_ Файл конфигурации docker-compose.

  - _nginx.conf:_ Файл кофнигурации Nginx.

В папке app:

  - _Dockerfile:_ Dockerfile для API.
  
  - _requirements.txt:_ Файл с необходимыми зависимостями API.

В папке bot:

  - _Dockerfile:_ Dockerfile для Telegram-Бота.

  - _requirements.txt:_ Файл с необходимыми зависимостями Telegram-Бота.

### Краткое описание работы проекта.

API имеет 2 эндпоинта для просмотра и отправки сообщений. Все сообщения валидируются при помощи модели Pydantic и хранятся в базе данных MongoDB. Подключено кэширование при помощи Redis.

**Документация к API:**

![image](https://github.com/user-attachments/assets/7a7a155d-beee-4b17-ba2f-1ba29a35e5bd)

Telegram-Бот работает в качестве отдельного приложения, с точки зрения кода, но фактически не может работать без API. Все взаимодействие с API осуществляется посредством HTTP-запросов. Telegram-Бот имеет 4 команды:

  - _/start:_ Стандартная команда для старта бота.

  ![image](https://github.com/user-attachments/assets/800494e4-9033-4ad6-a916-8a788cf894c9)

  - _/info:_ Команда с краткой информацией по работе бота.

  ![image](https://github.com/user-attachments/assets/b44116b1-1af1-451f-8689-966bf7f43da9)

  - _/send_ {message}: Для отправки сообщений.

  ![image](https://github.com/user-attachments/assets/90efcff9-b39d-4ae9-90c0-094093f28d71)

  - _/read:_ Для просмотра сообщений.

  ![image](https://github.com/user-attachments/assets/0bbf7877-0cb5-494c-8e97-8f2af3310989)

## Смешные моменты при разработке

![image](https://github.com/user-attachments/assets/7991ab8d-262a-4552-8783-b5946760e97e)

![image](https://github.com/user-attachments/assets/8aeb0226-e976-47a4-8a4b-01d324849caa)

![image](https://github.com/user-attachments/assets/251c42b7-f08d-484e-9183-3a5bae9811a2)
