from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.conf import settings


DB_UID = 'gghotted'
DB_UPWD = 'elwlahs2'


def index(request):
    return HttpResponse('Hello ajax')


def calc_form(request):
    return render(request, "ajax/calc.html")


def calc(request):
    op1 = int(request.GET["op1"])
    op2 = int(request.GET["op2"])
    result = op1 + op2
    return JsonResponse({"result": result})


def login_form(request):
    return render(request, "ajax/login.html")


def login(request):
    uid = request.GET['id']
    upwd = request.GET['pwd']
    if uid == DB_UID and upwd == DB_UPWD:
        request.session['user'] = uid
        return JsonResponse({'result': True})
    return JsonResponse({'result': False})


def upload_form(request):
    return render(request, "ajax/upload.html")


def upload(request):
    file = request.FILES['file1']
    filename = file._name
    fp = open(settings.BASE_DIR + "/static/" + filename, "wb")
    for chunk in file.chunks() :
        fp.write(chunk)
    fp.close()
    return HttpResponse("업로드 완료")


def run_python_form(request):
    return render(request, "ajax/run_python.html")


def run_python(request):
    code = request.GET['code']
    return HttpResponse(getPrinted(code).replace('\n', '<br>'))


glo = {}
loc = {}


def getPrinted(code):
    import sys
    import io

    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    exec(code, glo, loc)
    sys.stdout = old_stdout
    return buffer.getvalue()


