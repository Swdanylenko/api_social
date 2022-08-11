from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from user.renderers import UserJSONRenderer
from .serializers import RegisterSerializer, LoginSerializer, UserActivitySerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
  
  
class UserRegisterAPIView(GenericAPIView):
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
   
    def post(self, request):
        user = request.data.get('user')
        serializer = self.serializer_class(data=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class UserLoginAPIView(GenericAPIView):
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
      
    def post(self, request):
        user = request.data.get('user')
        serializer = self.serializer_class(data=user)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UserActivityAPIView(RetrieveUpdateAPIView): #/api/users
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserActivitySerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)