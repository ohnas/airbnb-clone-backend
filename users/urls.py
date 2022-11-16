from django.urls import path
from users.views import Me

urlpatterns = [
    path("me/", Me.as_view()),
]
