from django.urls import path
from . import views
from django.shortcuts import redirect, reverse


app_name = 'board'
urlpatterns = [
    path('', lambda request: redirect(reverse('board:manager', args=['common', '0', 'list']))),
    path('<category>/<int:pk>/<mode>', views.ViewManager.as_view(), name='manager'),
    path('logout', views.logout, name='logout'),
    path('login', views.LoginView.as_view(), name='login'),

    # test
    # path('', views.page_test),
    path('ajaxdel', views.ajax_delete),
    path('ajaxget', views.ajax_get),

    path('search/<category>/<int:page>', views.board_search),
    path('photo', views.PhotoView.as_view(), name='photo')
]
