from rest_framework import serializers
from rest_framework.serializers import Serializer
from api.serializers import CommentSerializer, PostCreatSerializer, PostSerializer
from blog.models import Comment, Post
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

class PostListView(ListAPIView):
    queryset = Post.objects.filter(status='published')
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('title','body',)
 


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.filter(status='published')
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, )


   

class PostCommentView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.filter(active = True)
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, )

   
    
class PostCommentCreatView(CreateAPIView):
    queryset = Comment.objects.filter(active = True)
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostCreatView(CreateAPIView):
    queryset = Comment.objects.filter(active = True)
    serializer_class = PostCreatSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

