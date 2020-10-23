from home.views import contactUs, home
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path("contactUs/", views.contactUs, name="contactUs"),
    path("aboutUs/", views.aboutUs, name="aboutUs"),
    path("houses/", views.houses, name="houses"),
    path('readMore/<str:slug>', views.readMore, name='readMore'),
]
