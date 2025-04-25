# Мой Блог на Django

[![Django](https://img.shields.io/badge/Django-5.2-green)](https://www.djangoproject.com)
[![Docker](https://img.shields.io/badge/Docker-OK-blue)](https://www.docker.com)

## 📌 Основные возможности
- Создание постов с тегами
- Комментарии и лайки
- Авторизация через JWT
- Кеширование в Redis

## 🚀 Быстрый старт

### Требования:
- Docker
- Python 3.11

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/ваш-логин/blog_platform.git

# 2. Перейдите в папку проекта
cd blog_platform

# 3. Запустите через Docker
docker-compose up --build

# 3.1 Доступы после запуска:
Сайт: http://localhost:8000
Админка: http://localhost:8000/admin

### 4. Сохраните файл (Ctrl+S)

---

## **Шаг 3: Создайте папку docs**

1. В корне проекта щёлкните правой кнопкой → "Создать" → "Папка"
2. Назовите её `docs`
3. Внутри создайте:
   - Папку `screenshots` (для картинок)
   - Файл `API.md` (правой кнопкой → Создать → Текстовый документ)
   - Файл `DEPLOY.md`

![Структура папок](https://i.imgur.com/5Xv4k7u.png)

---

## **Шаг 4: Добавьте скриншоты**

1. Сделайте скриншоты вашего блога:
   - Главная страница
   - Страница поста
   - Форма входа

2. Сохраните их в папку `docs/screenshots/`

3. Вставьте в README.md:
```markdown
## 📸 Скриншоты

| Главная | Пост | Комментарии |
|---------|------|-------------|
| ![Главная](docs/screenshots/home.png) | ![Пост](docs/screenshots/post.png) | ![Комменты](docs/screenshots/comments.png) |
