from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from bs4 import BeautifulSoup
import requests
from django.contrib import messages
from django.template import loader




def home_view(request, tag=None):
    if tag:
        posts = Post.objects.filter(tags__slug=tag) 
        tag = get_object_or_404(Tag, slug=tag)
    else:
        posts = Post.objects.all()
    
    categories = Tag.objects.all()

    context = {
        'posts': posts,
        'categories': categories,
        'tag': tag
    }

    return render(request, 'a_posts/home.html', context)


@login_required
def post_edit_view(request, pk):
    post = get_object_or_404(Post, id=pk, author=request.user)
    form = PostEditForm(instance=post) # prefills the form with the data from the post we passed
    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid:
            form.save()
            messages.success(request, 'Post updated!')
            return redirect('home')

    context = {
        'post': post,
        'form': form
    }

    print(f"Rendering post_edit.html for post: {post.title}")
    return render(request, 'a_posts/post_edit.html', context)


@login_required
def post_create_view(request):
    form = PostCreateForm()

    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            print(post.image)  # Debug print
            post.save()
            messages.success(request, 'Post created successfully')
            form.save_m2m()
            return redirect('home')
        else:
            messages.error(request, 'Error creating post')
    
    return render(request, 'a_posts/post_create.html', {'form': form})


@login_required 
def post_delete_view(request, pk):
    post = get_object_or_404(Post, id=pk, author=request.user)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted')
        return redirect('home')

    return render(request, 'a_posts/post_delete.html',
                  {'post': post})


def post_page_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'a_posts/post_page.html', {'post': post})