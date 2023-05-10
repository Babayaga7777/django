from django.urls import path
from first_app1 import views

urlpatterns = [
    path('',views.index,name='index'),
]