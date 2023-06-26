from rest_framework import serializers

class ArticleSerializer(serializers.Serializer):
    source = serializers.CharField(source='source.name')
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    url = serializers.URLField()
    urlToImage = serializers.URLField()
    publishedAt = serializers.DateTimeField()
    content = serializers.CharField()
