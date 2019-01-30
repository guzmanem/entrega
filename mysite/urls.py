from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('app_entrega/', include('app_entrega.urls')),
    path('admin/', admin.site.urls),
]
