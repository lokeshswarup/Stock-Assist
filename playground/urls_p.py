from django.urls import path
from . import views

# URL configuration 
urlpatterns = [
    path("hello/",views.say_hello),
    path("",views.index),
    path("news/",views.news),
    path("portfoliogenerator/",views.portfoliogenerator)
]
