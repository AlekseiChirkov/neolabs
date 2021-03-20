from datetime import datetime

from django.shortcuts import get_object_or_404

from apps.blog.models import Post


class PostService:
    model = Post

    @classmethod
    def get_active_posts(cls, request, obj, serializer):
        post = obj.all().filter(is_active=True)
        serializer = serializer(post, many=True)
        return serializer

    @classmethod
    def save_date_time(cls, request):
        post = get_object_or_404(cls.model, id=request.data.get('id'))
        post.date = datetime.now()
        post.save()
        return post
