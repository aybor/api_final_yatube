# Описание:
Проект api_final_yatube показывает как может быть устроен API для социальной сети yatube

В проекте можно посмотреть примеры:
* использования ViewSets;
* использования сериализаторов;
* разграничения прав доступа;
* создания пользовательского класса пагинации;
* использования JWT + Djoser для аутентификации пользователей;
* и многого другого.


# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/aybor/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

# Некоторые примеры запросов:

## Получение токена
### POST 
URL /api/v1/jwt/create/  
JSON
{
    "username": "user",
    "password": "password"
}
### Response
JSON
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNTc5MjU1MCwianRpIjoiNzI0YmY4Nzc3MDNmNDYwOTk1ZTRmMzg4NmQ0MzgyNjkiLCJ1c2VyX2lkIjoyfQ.Ofgo3Bv-t2Fj01HFKia_fP8N01IGnsu6N-858cdKVDg",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM1NzkyNTUwLCJqdGkiOiJhNzRiNDA2OWI3OTM0NTkzODAzMjQxMjIxZWI4N2E3MiIsInVzZXJfaWQiOjJ9.7Auocnm8bi8cZ3KT7z5EqoJ7yCOE6J0hn-u-VhIuNwo"
}

## Получение списка постов без пагинации
### GET 
URL /api/v1/posts/
### Response 
JSON [
    {
        "id": 1,
        "author": "aybor",
        "text": "123",
        "pub_date": "2021-10-31T18:12:20.610315Z",
        "image": null,
        "group": null
    },
    {
        "id": 2,
        "author": "user",
        "text": "2",
        "pub_date": "2021-10-31T18:12:26.864969Z",
        "image": null,
        "group": null
    },
    {
        "id": 3,
        "author": "user",
        "text": "test text",
        "pub_date": "2021-10-31T18:57:19.186396Z",
        "image": null,
        "group": null
    }
]

## Получение списка постов с пагинацией
### GET 
URL /api/v1/posts/?limit=2&offset=1
### Response
JSON {
    "count": 3,
    "next": null,
    "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=2",
    "results": [
        {
            "id": 2,
            "author": "user",
            "text": "2",
            "pub_date": "2021-10-31T18:12:26.864969Z",
            "image": null,
            "group": null
        },
        {
            "id": 3,
            "author": "user",
            "text": "test text",
            "pub_date": "2021-10-31T18:57:19.186396Z",
            "image": null,
            "group": null
        }
    ]
}
## Подписка на другого пользователя
### POST
URL /api/v1/follow/  
JSON {
    "following": "user2"
}
### Response
JSON {
    "id": 2,
    "following": "user2"
}
