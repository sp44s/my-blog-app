from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    post = Post.objects.all()
    return render( request, 'blog/post_list.html', {'NamedPosts':post})

    