from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    post = Post.objects.all()
    return render( request, 'blog/post_list.html', {'NamedPosts':post})


def post_detail(request, id):
    post = get_object_or_404( Post, pk=id)
    return render( request, 'blog/post_detail.html', {'onepost':post})