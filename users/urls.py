from django.urls import path
from users.views import (
    Me,
    Users,
    ChangePassword,
    PublicUser,
    LogIn,
    LogOut,
    GithubLogIn,
)

urlpatterns = [
    path("", Users.as_view()),
    path("me/", Me.as_view()),
    path("change-password/", ChangePassword.as_view()),
    path("log-in/", LogIn.as_view()),
    path("log-out/", LogOut.as_view()),
    path("github", GithubLogIn.as_view()),
    path("@<str:username>/", PublicUser.as_view()),
]
