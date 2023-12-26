from rest_framework import routers,serializers,viewsets
from .models import Article

class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    published = serializers.DateTimeField(format="%m/%d/%Y %I:%M%p", read_only=True)

    class Meta:
        model = Article
        fields = ['title', 'body', 'author', 'category', 'image_url', 'origin_url', 'published', 'id']