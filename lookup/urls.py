from django.urls import path
from . import views
urlpatterns = [
    path('', views.weather, name="weather"),
    path('air_quality', views.air_quality, name='air_quality'),
    path('about.html', views.about, name="about"),
    path('jumbotron.html', views.jumbotron, name="jumbotron")
]
