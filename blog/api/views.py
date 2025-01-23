from rest_framework import generics

from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

from blog.api.serializers import PostSerializer
from blog.models import Post 

class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer 

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
  queryset = Post.objects.all()
  serializer_class = PostSerializer

  def get(self, request, *args, **kwargs):
    return super(PostDetail, self).get(request, *args, **kwargs) 

