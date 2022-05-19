
from django.contrib import admin
from django.urls import path
from Bolim1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', all_students),
    # path('muallif/', barcha_mualliflar),




]
