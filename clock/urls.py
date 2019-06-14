from django.urls import path
from . import views

urlpatterns = [
    path('', views.anlgClock, name='anlgClock'),
]