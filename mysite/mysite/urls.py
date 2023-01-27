from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('pickmywaste/', include('pickmywaste.urls')),
    path('admin/', admin.site.urls),

]