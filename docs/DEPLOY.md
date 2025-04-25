## **Шаг 6: Создайте DEPLOY.md**

1. Откройте `docs/DEPLOY.md`
2. Вставьте:
```markdown
# Деплой проекта

## Production-настройки

1. Создайте файл `.env`:
```ini
SECRET_KEY=ваш_ключ
DEBUG=0

2.Запустите:
docker-compose -f docker-compose.prod.yml up --build -d

# Проверить логи
docker-compose logs web

# Остановить проект
docker-compose down

##  Проверьте результат