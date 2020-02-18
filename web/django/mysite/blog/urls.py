from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    # function base
    path('<int:pk>/detail', views.detail, name='detail'),
    path('list', views.list, name='list'),
    path('logout', views.logout, name='logout'),

    # class base
    path('add', views.PostView.as_view(), name='add'),
    path('login', views.LoginView.as_view(), name='login'),
    path('<int:pk>/edit', views.EditView.as_view(), name='edit'),
]
