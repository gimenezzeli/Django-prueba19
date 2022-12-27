from django.contrib import admin
from django.urls import path

from project_family.views import vista_template
from family.views import create_familiar, list_familiar

urlpatterns = [
    path('admin/', admin.site.urls),

    path('vista-template/', vista_template),

    path('create-familiar/', create_familiar),
    path('list-familiar/', list_familiar),
]