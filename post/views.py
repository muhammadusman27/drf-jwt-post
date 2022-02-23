import imp
from django.shortcuts import render

from rest_framework import viewsets
from .models import MyPost
from .serializers import MyPostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


# Create your views here.


@permission_classes((IsAuthenticated, ))
class MyPostView(viewsets.ModelViewSet):
    queryset = MyPost.objects.all()
    serializer_class = MyPostSerializer


