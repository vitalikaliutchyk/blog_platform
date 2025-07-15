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
```

### Обновить токен
```http
POST /api/token/refresh/
Content-Type: application/json

{
    "refresh": "your-refresh-token"
}
```

## 📝 Посты

### Получить список постов
```http
GET /api/posts/
Authorization: Bearer <token>
```

**Ответ:**
```json
[
    {
        "id": 1,
        "title": "Пример поста",
        "content": "Содержание поста...",
        "author": {
            "id": 1,
            "username": "admin",
            "role": "admin"
        },
        "created_at": "2024-01-01T12:00:00Z",
        "likes_count": 5,
        "tags": []
    }
]
```

### Создать пост
```http
POST /api/posts/
Authorization: Bearer <token>
Content-Type: application/json

{
    "title": "Новый пост",
    "content": "Содержание поста",
    "tags": [1, 2]
}
```

### Лайкнуть/убрать лайк
```http
POST /api/posts/{id}/like/
Authorization: Bearer <token>
```

**Ответ:**
```json
{
    "likes_count": 6,
    "liked": true
}
```

## 💬 Комментарии

### Получить комментарии поста
```http
GET /api/comments/?post={post_id}
Authorization: Bearer <token>
```

### Создать комментарий
```http
POST /api/comments/
Authorization: Bearer <token>
Content-Type: application/json

{
    "post": 1,
    "text": "Отличный пост!"
}
```

## 🏷️ Теги

### Получить все теги
```http
GET /api/tags/
```

## 📊 Статистика

### Просмотры поста
```http
GET /api/posts/{id}/views/
```

## 🔧 Swagger UI

Доступен по адресу: `http://localhost:8000/swagger/`
