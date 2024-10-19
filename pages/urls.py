from django.urls import path
from .views import *

urlpatterns = [
    path("first/", homePageView, name="first"),
    path("second/", homePageView2, name="second"),
    path("third/", homePageView3, name="third"),
]