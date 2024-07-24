from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from bs4 import BeautifulSoup
import requests
from django.contrib import messages
from django.template import loader


def home_view(request):
    posts = Post.objects.all()
    return render(request, 'a_posts/home.html', {'posts': posts})








def post_edit_view(request, pk):
    post = get_object_or_404(Post, id=pk)

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




def post_create_view(request):
    form = PostCreateForm()

    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            print(post.image)  # Debug print
            post.save()
            messages.success(request, 'Post created successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error creating post')
    
    return render(request, 'a_posts/post_create.html', {'form': form})


def post_delete_view(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted')
        return redirect('home')

    return render(request, 'a_posts/post_delete.html',
                  {'post': post})


def post_page_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'a_posts/post_page.html', {'post': post})