from django.urls import path
from categories.views import categories, category

urlpatterns = [
    path("", categories),
    path("<int:pk>/", category),
]
