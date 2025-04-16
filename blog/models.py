from django.db import models
from django.contrib.auth import get_user_model
from django.core.cache import cache

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

    # Методы для работы с просмотрами через Redis
    def increment_views(self):
        key = f"post_views:{self.id}"

        if not cache.has_key(key):
            cache.set(key, 0)

        try:
            cache.incr(key)
        except ValueError:
            cache.set(key, 1)

    @property
    def views(self):
        return cache.get(f"post_views:{self.id}", 0)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий от {self.author}"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name