from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import RegisterSerializer, PostSerializer, CommentSerializer, LikeSerializer
from .models import *
from .permissions import IsOwnerOrReadOnly
# from rest_framework.permissions import IsAuthenticated

from django.views.generic import TemplateView
from rest_framework.pagination import PageNumberPagination
# Create your views here.

#Register view
class RegisterUser(generics.GenericAPIView, TemplateView):
    serializer_class = RegisterSerializer
    template_name = "signup.html"

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email
        })


class PostView(viewsets.ModelViewSet, TemplateView):
    template_name = 'all_post.html'
    pagination_class = PageNumberPagination
    page_size = 2
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentView(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeView(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
