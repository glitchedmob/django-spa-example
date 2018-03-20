from rest_framework import serializers

from message_board.models import Post

class PostSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    body = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.data.get('title', instance.title)
        instance.body = validated_data.data.get('body', instance.body)
