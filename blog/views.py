import logging

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone 

from blog.models import Post
from blog.forms import CommentForm

# Create your views here.

logger = logging.getLogger(__name__)

def get_ip(request):
  # 192.168.10.226
  from django.http import HttpResponse 
  return HttpResponse(request.META['REMOTE_ADDR'])

def index(request):
  posts = Post.objects.filter(published_at__lte=timezone.now()).select_related("author")
  logger.debug("Got %d posts", len(posts))
  return render(request, "blog/index.html", {"posts": posts})

def post_detail(request, slug):
  post = get_object_or_404(Post, slug=slug)
  if request.user.is_active:
    if request.method == "POST":
      comment_form = CommentForm(request.POST)

      if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.content_object = post 
        comment.creator = request.user 
        comment.save() 
        logger.info("Created comment on Post %d for user %s", post.pk, request.user)
        # Always redirect after saving content to the database
        return redirect(request.path_info)
      # What should I do if the form is invalid

    else:
      comment_form = CommentForm()
  else:
    # Do this if the user is inactive(Anonymous Users-users that aren't logged in)
    comment_form = None 
  
  return render(request, "blog/post-detail.html", {"post":post, "comment_form":comment_form})