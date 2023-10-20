
<h1 align="center"> Асинронный Web-сервис получения вопросов викторины </h1>

___
### Используемый стек<a name="stack"></a>

[![Python][Python-badge]][Python-url]
[![FastAPI][Fastapi-badge]][Fastapi-url]
[![Docker][Docker-badge]][Docker-url]
[![Postgres][Postgres-badge]][Postgres-url]

### Системные требования
- Python 3.11+;
- Docker (19.03.0+) c docker compose;
- [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer).

<h2>Подготовка проекта к запуску</h2>

Заполнить .env-файл, вариант заполнения указан example.env.


<h2>Запуск проекта</h2>

**1. Из корневой папки запустить docker-compose командой:**
```shell
docker-compose up
```

или для пересборки
```shell
docker-compose up -d --build
```
Миграции alembic будут применены автоматически.


<h2>Техническая документация</h2>

Доступ к Swagger:

http://127.0.0.1/docs/


<h2>Как работать с API сервиса</h2>

**Пользователь отправляет POST-запрос с параметром questions_num в котором
указывает количество вопросов на эндпоинт
/api/questions/, в ответе на запрос ему приходит список сохраненных в базе
данных вопросов викторины**

*Пример:*
```
POST localhost/api/questions/
Content-Type: application/json

{
  "questions_num": 1
}
```
В случае отсутвия вопросов в базе данных возвращается пустой список.

<!-- MARKDOWN LINKS & BADGES -->

[Python-url]: https://www.python.org/

[Python-badge]: https://img.shields.io/badge/Python-376f9f?style=for-the-badge&logo=python&logoColor=white

[Fastapi-url]: https://fastapi.tiangolo.com/

[Fastapi-badge]: https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white

[Docker-url]: https://www.docker.com/

[Docker-badge]: https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white

[Postgres-url]: https://www.postgresql.org/

[Postgres-badge]: https://img.shields.io/badge/postgres-306189?style=for-the-badge&logo=postgresql&logoColor=white
