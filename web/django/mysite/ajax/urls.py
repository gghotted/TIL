from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('calcform', views.calc_form),
    path('calc', views.calc),
    path('loginform', views.login_form),
    path('login', views.login),
    path('uploadform', views.upload_form),
    path('upload', views.upload),
    path('runpythonform', views.run_python_form),
    path('runpython', views.run_python),
]
