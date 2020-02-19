from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('board/', include('board.urls')),
    path('blog/', include('blog.urls')),
    path('ajax/', include('ajax.urls')),
    path('', include('myapp.urls')),
    path('admin/', admin.site.urls),
]
