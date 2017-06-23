from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import Postform

def post_list(request):
    post = Post.objects.all()
    return render( request, 'blog/post_list.html', {'NamedPosts':post})


def post_detail(request, id):
    post = get_object_or_404( Post, pk=id)
    return render( request, 'blog/post_detail.html', {'onepost':post})
    
    
def post_new(request):
    if (request.method == "POST"):
        form = Postform(request.POST)
        if (form.is_valid()):
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.pk)
    else:
        form = Postform()
    return render( request, 'blog/post_edit.html', {'newform':form})

def post_edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = Postform(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.pk)
    else:
        form = Postform(instance=post)
    return render(request, 'blog/post_edit.html', {'newform': form})
    


    
    