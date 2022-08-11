from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer, PostCreateSerializer, LikeByDaySerializer, VoteSerializer
from rest_framework.generics import GenericAPIView
from user.renderers import PostJSONRenderer, VoteJSONRenderer
from django.db.models.functions import TruncDay
from post.models import Vote, Post
from django.db.models import Count

class PostsView(GenericAPIView):
        permission_classes = (AllowAny,)
        renderer_classes = (PostJSONRenderer,)
        serializer_class = PostSerializer
        queryset = Post.objects.all()

        def get(self, request):
            serializer = self.serializer_class(self.get_queryset(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
                
class PostCreateView(GenericAPIView):
        permission_classes = (IsAuthenticated,)
        serializer_class = PostCreateSerializer
        
        def post(self, request):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(user_added=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostVoteView(GenericAPIView):
        permission_classes = (IsAuthenticated,)
        serializer_class = VoteSerializer
        renderer_classes = (VoteJSONRenderer,)
        
        def post(self, request):
            data = request.data.get('vote', None)
            post = Post.objects.filter(pk=data.get('id', None)) 
            if post.exists():
                if not request.user in post.get().votes.all():
                    vote = Vote(post=post.get(), user=request.user)
                    vote.save()
                else:
                    vote = Vote.objects.get(post=post.get(), user=request.user)
                    vote.delete()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST) # no post found
            
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
class PostAnalitics(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LikeByDaySerializer
    queryset = Vote.objects.all()
    
    def get(self, request):
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')
        votes = Vote.objects.annotate(day=TruncDay('date_voted')).filter(day__range=[date_from, date_to]).values('day').annotate(votes=Count('pk')).values('day', 'votes') 
        serializer = self.serializer_class(votes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)