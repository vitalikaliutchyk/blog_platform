from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from blog.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user

        if not user.is_authenticated:
            return Response({"error": "Авторизация требуется"}, status=status.HTTP_401_UNAUTHORIZED)

        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
            liked = False
        else:
            post.likes.add(user)
            liked = True

        return Response({
            'likes_count': post.likes.count(),
            'liked': liked
        })
