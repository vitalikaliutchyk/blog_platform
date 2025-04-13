from django.shortcuts import render
from blog.models import Post

def post_list(request):
    posts = Post.objects.prefetch_related('comments').all()
    for post in posts:
        post.increment_views()

    return render(request, 'blog/post_list.html', {'posts': posts})
