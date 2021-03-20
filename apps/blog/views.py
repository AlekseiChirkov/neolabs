from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializers import PostSerializer, PostCategorySerializer, AuthorSerializer
from .models import Post, PostCategory, Author
from .services import PostService


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        serializer = PostService.get_active_posts(request, self.queryset, self.serializer_class)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data,
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        PostService.save_date_time(request)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostCategoryViewSet(viewsets.ModelViewSet):
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


