from django.urls import path
from rooms.views import say_hello

urlpatterns = [
    path("", say_hello),
]
