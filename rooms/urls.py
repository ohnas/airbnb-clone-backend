from django.urls import path
from rooms.views import Amenities, AmenityDetail


urlpatterns = [
    path("amenities/", Amenities.as_view()),
    path("amenities/<int:pk>/", AmenityDetail.as_view()),
]
