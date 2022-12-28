from django.contrib import admin
from django.urls import path

from Familia_Glez.views import nombre_familiar, vista_con_template

from products.views import create_familiar, list_familiar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Familiar/',nombre_familiar),
    path('vista-con-template/', vista_con_template),

    path('create-familiar/',create_familiar),
    path('list-familiar/',list_familiar)
]
