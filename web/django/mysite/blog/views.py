from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.contrib.auth import authenticate, login, logout as loggedout
from django.views.generic import View
from blog.models import Post
from django.forms import Form, CharField, Textarea, ValidationError


def detail(request, pk):
    post = get_object_or_404(Post, id=pk)  # id or pk
    return render(request, "blog/detail.html", {"post": post})


def list(request):
    posts = Post.objects.all()
    if request.user.is_authenticated:
        posts = posts.filter(author=request.user)
    return render(request, "blog/list.html", {"posts": posts})


def logout(request):
    loggedout(request)
    return redirect('blog:list')


class PostView(View):
    # method 가 get 일 때 실행되는 함수
    def get(self, request):
        form = PostForm()
        return render(request, "blog/edit.html", {'form': form})

    # method 가 post 일 때 실행되는 함수
    def post(self, request):
        params = {'title': request.POST['title'],
                  'text': request.POST['text'],
                  'author': request.user}
        Post(**params).save()
        return redirect('blog:list')


# (create & Update) view
# https://stackoverflow.com/questions/17192737/django-class-based-view-for-both-create-and-update
class EditView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        form = PostForm(initial={'title': post.title, 'text': post.text})
        return render(request, 'blog/edit.html', {'form': form, 'pk': pk})

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form['title'].value()
            post.text = form['text'].value()
            post.publish()
            return redirect('blog:list')
        return render(request, 'blog/edit.html', {'form': form, 'pk': pk})


class LoginView(View):
    def get(self, request):
        return render(request, 'blog/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('blog:list')
        return redirect('blog:login')


# custom validator
def validator(value):
    if len(value) <= 5:
        raise ValidationError('너무 짧아요.')


class PostForm(Form):
    title = CharField(label='제목', max_length=20, validators=[validator])
    text = CharField(label='내용', widget=Textarea)
