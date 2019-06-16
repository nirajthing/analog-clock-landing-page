from django.urls import path
from . import views

urlpatterns = [
    path('', views.anlgClock, name='anlgClock'),
    path('next_page',views.nextpage, name='nextpage'),
    
]