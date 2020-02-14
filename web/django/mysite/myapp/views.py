from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .faceverification import face_verification

DB_UID = 'gghotted'
DB_UPWD = 'elwlahs2'


def index(request):
    return HttpResponse('hello django')


def test(request):
    content = {
        'dict': {'사과': 500, '바나나': 2000, '파인애플': 3400},
        'list': [1, 2, 3, 4],
    }
    return render(request, 'template.html', content)


def login(request):
    uid = request.GET['id']
    upwd = request.GET['pwd']

    if uid == DB_UID and upwd == DB_UPWD:
        request.session['user'] = uid
        return redirect('/service')
    return redirect("/static/login.html")


def service(request):
    if request.session.get('user'):
        return HttpResponse('main service')
    else:
        return redirect("/static/login.html")


@csrf_exempt
def uploadimage(request):
    file = request.FILES['img']
    filename = file._name
    fp = open(settings.BASE_DIR + "/static/" + filename, "wb")
    for chunk in file.chunks():
        fp.write(chunk)
    fp.close()
    html = "ok :" + "^^" + filename

    result = face_verification(settings.BASE_DIR + "/static/" + filename)
    if result != "" :
        request.session["user"] = result
        return redirect("/service")
    return redirect("/static/login.html")
