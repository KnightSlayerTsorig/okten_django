from django.contrib import admin
from django.urls import path

from calculator.views import home, calculator

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('<str:f_num>/<str:action>/<str:s_num>', calculator)
]
