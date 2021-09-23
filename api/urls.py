from api.views import PostCommentCreatView, PostCommentView, PostCreatView, PostDetailView, PostListView
from django.urls import path


urlpatterns = [
    path('',PostListView.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
    path('comment/<int:pk>/', PostCommentView.as_view()),
    path('comment/creat/', PostCommentCreatView.as_view()),
    path('creat/post/',PostCreatView.as_view()),
]