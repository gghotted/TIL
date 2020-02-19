from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.contrib.auth import authenticate, login, logout as loggedout
from django.views.generic import View
from django.conf import settings
from . import models
from . import forms


# Create, Edit 한개의 View 클래스로 처리
class ViewManager(View):
    def get(self, request, mode, pk, category):
        if mode == 'list':
            posts = models.Board.objects.all()
            if request.user.is_authenticated:
                posts = posts.filter(author=request.user)
            if category:
                posts = posts.filter(category=category)
            return render(request, "board/list.html", {'posts': posts})

        elif mode == 'detail':
            post = get_object_or_404(models.Board, pk=pk)  # id or pk
            post.views += 1
            post.save()
            return render(request, "board/detail.html", {"post": post})

        elif mode == 'add':
            form = forms.BoardForm()
            return render(request, 'board/edit.html', {'form': form})

        elif mode == 'edit':
            post = get_object_or_404(models.Board, pk=pk)
            form = forms.BoardForm(instance=post)
            return render(request, 'board/edit.html', {'form': form})

        else:
            return HttpResponse('ERROR PAGE')

    def post(self, request, mode, pk, category):
        if mode == 'add':
            form = forms.BoardForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.category = category
                post.save()
                return redirect(reverse('board:manager', args=[category, 0, 'list']))
            return render(request, 'board/edit.html', {'form': form})

        elif mode == 'edit':
            form = forms.BoardForm(request.POST, instance=models.Board.objects.get(pk=pk))
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect(reverse('board:manager', args=[category, 0, 'list']))
            return render(request, 'board/edit.html', {'form': form})

        else:
            return HttpResponse('ERROR PAGE')


class LoginView(View):
    def get(self, request):
        return render(request, 'board/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('board:manager', args=['common', 0, 'list']))
        return redirect('board:login')


def logout(request):
    loggedout(request)
    return redirect(reverse('board:manager', args=['common', 0, 'list']))