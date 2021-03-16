from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Post, Author, PostCategory


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, required=False)
    category = PostCategorySerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'owner', 'author', 'category']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        category_data = validated_data.pop('category')
        post = Post.objects.create(**validated_data)
        author_data_list = []
        category_data_list = []
        for author, category in zip(author_data, category_data):
            author_data_list.append(
                Author(
                    post_id=post.id,
                    **author
                )
            )
            category_data_list.append(
                PostCategory(
                    post_id=post.id,
                    **category
                )
            )
        print(author_data)
        print(category_data)
        Author.objects.bulk_create(author_data_list)
        PostCategory.objects.bulk_create(category_data_list)
        post.save()
        return post
