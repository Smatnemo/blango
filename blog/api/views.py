from rest_framework import generics

from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer
from blog.models import Post 
from blango_auth.models import User

class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer 

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
  queryset = Post.objects.all()
  serializer_class = PostDetailSerializer

  def get(self, request, *args, **kwargs):
    return super(PostDetail, self).get(request, *args, **kwargs) 

class UserDetail(generics.RetrieveAPIView):
  lookup_field = "email"
  queryset = User.objects.all()
  serializer_class = UserSerializer

