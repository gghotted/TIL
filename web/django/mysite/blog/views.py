from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.contrib.auth import authenticate, login, logout as loggedout
from django.views.generic import View
from blog.models import Post
from .forms import PostForm


def logout(request):
    loggedout(request)
    return redirect(reverse('blog:manager', args=['list']))


# Create, Edit 한개의 View 클래스로 처리
class ViewManager(View):
    def get(self, request, mode, pk=None):
        if mode == 'list':
            posts = Post.objects.all()
            if request.user.is_authenticated:
                posts = posts.filter(author=request.user)
            return render(request, "blog/list.html", {"posts": posts})

        elif mode == 'detail':
            post = get_object_or_404(Post, id=pk)  # id or pk
            return render(request, "blog/detail.html", {"post": post})

        elif mode == 'add':
            form = PostForm()
            return render(request, 'blog/edit.html', {'form': form})

        elif mode == 'edit':
            post = get_object_or_404(Post, pk=pk)
            form = PostForm(instance=post)
            return render(request, 'blog/edit.html', {'form': form})

        else:
            return HttpResponse('ERROR PAGE')

    def post(self, request, pk, mode):
        if mode == 'add':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect(reverse('blog:manager', args=['list']))
            return render(request, 'blog/edit.html', {'form': form})

        elif mode == 'edit':
            form = PostForm(request.POST, instance=Post.objects.get(pk=pk))
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                print('reverse only : ', reverse('blog:manager', args=['list']))
                print('reverse & redirect : ', redirect(reverse('blog:manager', args=['list'])))
                return redirect(reverse('blog:manager', args=['list']))
            return render(request, 'blog/edit.html', {'form': form})

        else:
            return HttpResponse('ERROR PAGE')


class LoginView(View):
    def get(self, request):
        return render(request, 'blog/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('blog:manager', args=['list']))
        return redirect('blog:login')

