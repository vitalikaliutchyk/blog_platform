# 🚀 Django Blog Platform

[![Django](https://img.shields.io/badge/Django-5.2-green)](https://www.djangoproject.com)
[![Docker](https://img.shields.io/badge/Docker-OK-blue)](https://www.docker.com)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org)
[![DRF](https://img.shields.io/badge/DRF-3.16.0-orange)](https://www.django-rest-framework.org)

## 📌 Основные возможности

- ✨ **Создание постов** с тегами и форматированием
- 💬 **Система комментариев** с авторизацией
- ❤️ **Лайки и дизлайки** постов
- 👥 **Система ролей** (Автор, Модератор, Админ)
- 🔐 **JWT аутентификация** для API
- 📊 **Счетчик просмотров** через Redis
- 🎨 **Современный UI** с Bootstrap 5
- 📱 **REST API** с полной документацией
- 🐳 **Docker** контейнеризация

## 🚀 Быстрый старт

### Вариант 1: Локальная разработка

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/ваш-логин/blog_platform.git
cd blog_platform

# 2. Создайте виртуальное окружение
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

# 3. Установите зависимости
pip install -r requirements.txt

# 4. Примените миграции
python manage.py migrate

# 5. Создайте суперпользователя
python manage.py createsuperuser

# 6. Запустите сервер
python manage.py runserver
```

### Вариант 2: Docker (рекомендуется)

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/ваш-логин/blog_platform.git
cd blog_platform

# 2. Запустите через Docker Compose
docker-compose up --build

# 3. В отдельном терминале создайте суперпользователя
docker-compose exec web python manage.py createsuperuser
```

## 🌐 Доступы после запуска

| Сервис | URL | Описание |
|--------|-----|----------|
| **Сайт** | http://localhost:8000 | Главная страница блога |
| **Админка** | http://localhost:8000/admin | Панель администратора |
| **API** | http://localhost:8000/api/ | REST API |
| **Swagger** | http://localhost:8000/swagger/ | API документация |
| **Redoc** | http://localhost:8000/redoc/ | Альтернативная API документация |

## 🔧 Тестирование

```bash
# Запуск Django тестов
python manage.py test
```

## 📚 API Документация

Полная документация API доступна в файле [docs/API.md](docs/API.md)

### Основные эндпоинты:

- `GET /api/posts/` - Список постов
- `POST /api/posts/` - Создание поста
- `POST /api/posts/{id}/like/` - Лайк поста
- `GET /api/comments/` - Список комментариев
- `POST /api/token/` - Получение JWT токена

## 🏗️ Архитектура проекта

```
blog_platform/
├── blog/                 # Основное приложение блога
│   ├── models.py        # Модели Post, Comment, Tag
│   ├── views.py         # Представления для веб-интерфейса
│   └── forms.py         # Формы для создания постов
├── api/                  # REST API приложение
│   ├── viewsets.py      # ViewSets для API
│   └── serializers.py   # Сериализаторы
├── users/               # Пользователи и аутентификация
│   └── models.py        # Кастомная модель User
├── templates/           # HTML шаблоны
├── static/              # Статические файлы (CSS, JS)
└── docs/               # Документация
```

## 🔐 Аутентификация

### Веб-интерфейс
- Сессионная аутентификация
- Регистрация и вход через формы

### API
- JWT токены
- Access Token (30 минут)
- Refresh Token (7 дней)

## 🛠️ Технологический стек

- **Backend**: Django 5.2, Django REST Framework
- **Database**: PostgreSQL (production), SQLite (development)
- **Cache**: Redis
- **Authentication**: JWT (Simple JWT)
- **Frontend**: Bootstrap 5, jQuery
- **Documentation**: Swagger/OpenAPI
- **Deployment**: Docker, Gunicorn

## 📊 Функциональность

### Для пользователей:
- ✅ Регистрация и авторизация
- ✅ Создание и редактирование постов
- ✅ Добавление комментариев
- ✅ Лайки постов
- ✅ Просмотр статистики

### Для модераторов:
- ✅ Модерация комментариев
- ✅ Управление тегами

### Для администраторов:
- ✅ Полный доступ к админке
- ✅ Управление пользователями
- ✅ Системные настройки

## 🚀 Развертывание в production

1. **Настройте переменные окружения:**
   ```bash
   SECRET_KEY=your-secret-key
   DEBUG=False
   DATABASE_URL=postgres://user:pass@host:port/db
   REDIS_URL=redis://host:port/1
   ```

2. **Соберите статические файлы:**
   ```bash
   python manage.py collectstatic
   ```

3. **Запустите через Docker:**
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для новой функции
3. Внесите изменения
4. Добавьте тесты
5. Создайте Pull Request

## 📝 Лицензия

MIT License - см. файл [LICENSE](LICENSE)

## 📞 Поддержка

- 📧 Email: support@example.com
- 💬 Issues: [GitHub Issues](https://github.com/ваш-логин/blog_platform/issues)
- 📖 Документация: [docs/](docs/)

---

⭐ **Если проект вам понравился, поставьте звездочку!**
