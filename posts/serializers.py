from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(required=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'tags', 'created_at', 'user_id']

    def validate(self, data):
        if 'title' not in data or 'content' not in data:
            raise serializers.ValidationError("Title and content are required.")
        if 'user_id' not in data:
            raise serializers.ValidationError("User ID is required.")
        return data