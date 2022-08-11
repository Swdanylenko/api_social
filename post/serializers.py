from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta():
        model = Post
        fields = ('id', 'title', 'body', 'user_added')
    
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta():
        model = Post
        fields = ('title', 'body', 'user_added')
    
    def validate(self, data):
        title = data.get('title', None)
        body = data.get('body', None)
        
        return {
        'title': title,
        'body': body,
    }

    
class VoteSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=255)
    class Meta():
        model = Post
        fields = ('id', 'votes')
        
    def validate(self, data):
        id = data.get('id', None)
        votes = Post.objects.get(pk=id).votes
        return {
            'id': id,
            'votes': votes}

    
class LikeByDaySerializer(serializers.Serializer):
    day = serializers.DateTimeField()
    votes = serializers.IntegerField()

    class Meta:

        fields = ('day', 'votes')