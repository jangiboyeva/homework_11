from django.shortcuts import render
from .models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .serializers import Userserializers
from .permissions import UserPermission

class UserView(ModelViewSet):
    serializer_class = Userserializers
    permission_classes = [UserPermission]
    
    def get_queryset(self):
        queryset = User.objects.filter(user_id=self.kwargs['pk'])
        return queryset