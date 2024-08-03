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

Проект построен следующим образом:

### Структура проекта

![image](https://github.com/user-attachments/assets/aae79f4b-5fa4-4060-9712-9bde5e2761b0)

#### Файлы кода

**В папке app находится код API на FastAPI:**

  - routers/messages.py: Маршрутизатор сообщений.

  - config.py: Параметры приложения (Извлечение данных из .env).

  - database.py: Взаимодейтсвие с MongoDB.

  - models.py: Модели Pydantic для валидации.

  - main.py: Точка входа для API.

**В папке bot находится код Telegram-Бота на Aiogram3:**

  - handlers.py: Маршрутизатор сообщений с обработчиками.

  - config.py: Параметры бота (Извлечение данных из .env).

  - main.py: Точка входа для Бота.

#### Оставшиеся файлы

В корне проекта:

  - .env: Файл с настройками для всего приложения (Не экспортируется на GitHub в целях безопасности).

  - .gitignore: Файл с указанием игнорирования папок и файлов для системы контроля версий Git.

  - docker-compose.yml: Файл конфигурации docker-compose.

  - nginx.conf: Файл кофнигурации Nginx.

В папке app:

  - Dockerfile: Dockerfile для API.
  
  - requirements.txt: Файл с необходимыми зависимостями API.

В папке bot:

  - Dockerfile: Dockerfile для Telegram-Бота.

  - requirements.txt: Файл с необходимыми зависимостями Telegram-Бота.

### Краткое описание работы проекта.

API имеет 2 эндпоинта для просмотра и отправки сообщений. Все сообщения валидируются при помощи модели Pydantic и хранятся в базе данных MongoDB. Подключено кэширование при помощи Redis.

**Документация к API:**

![image](https://github.com/user-attachments/assets/7a7a155d-beee-4b17-ba2f-1ba29a35e5bd)

Telegram-Бот работает в качестве отдельного приложения, с точки зрения кода, но фактически не может работать без API. Все взаимодействие с API осуществляется посредством HTTP-запросов. Telegram-Бот имеет 4 команды:

  - /start: Стандартная команда для старта бота.

  ![image](https://github.com/user-attachments/assets/800494e4-9033-4ad6-a916-8a788cf894c9)

  - /info: Команда с краткой информацией по работе бота.

  ![image](https://github.com/user-attachments/assets/b44116b1-1af1-451f-8689-966bf7f43da9)

  - /send {message}: Для отправки сообщений.

  ![image](https://github.com/user-attachments/assets/90efcff9-b39d-4ae9-90c0-094093f28d71)

  - /read: Для просмотра сообщений.

  ![image](https://github.com/user-attachments/assets/0bbf7877-0cb5-494c-8e97-8f2af3310989)


  
