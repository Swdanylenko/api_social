from django.db import models
import jwt
from django.conf import settings
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=30, unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)
    last_request = models.DateTimeField(null=True)
    
    USERNAME_FIELD = 'email'
    objects =  UserManager()
    
    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=1)
    
        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')
    
        return token.decode('utf-8')
    
    @property
    def token(self):
        return self._generate_jwt_token()