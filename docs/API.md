# API Documentation

## 🔑 Аутентификация

### Получить токен
```http
POST /api/token/
Content-Type: application/json

{
    "username": "user",
    "password": "pass123"
}


# 1. 📝 Посты
Список постов:
'''http
GET /api/posts/
Content-Type: application/json

[
    {
        "id": 1,
        "title": "Пример поста",
        "author": "admin"
    }
]
