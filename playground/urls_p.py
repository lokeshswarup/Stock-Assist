from django.urls import path
from . import views

# URL configuration 
urlpatterns = [
    path("",views.index),
    path("news/",views.news),
    path("portfoliogenerator/",views.portfoliogenerator),
    path("portfolioccp/",views.portfolioccp),
    path("portfoliobw/",views.portfoliobw),
    path("portfoliofii/",views.portfoliofii),
    path("portfoliol/",views.portfoliol),
    path("aboutus/",views.about)
]
