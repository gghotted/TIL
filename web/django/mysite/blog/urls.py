from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    # function base

    path('logout', views.logout, name='logout'),

    # class base
    path('login', views.LoginView.as_view(), name='login'),
    path('<int:pk>/<mode>', views.ViewManager.as_view(), name='manager'),
    path('<mode>', views.ViewManager.as_view(), name='manager'),
]
