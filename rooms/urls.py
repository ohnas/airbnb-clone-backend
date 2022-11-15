from django.urls import path
from rooms.views import (
    Amenities,
    AmenityDetail,
    Rooms,
    RoomDetail,
    RoomReviews,
    RoomAmenities,
)


urlpatterns = [
    path("", Rooms.as_view()),
    path("<int:pk>/", RoomDetail.as_view()),
    path("<int:pk>/reviews", RoomReviews.as_view()),
    path("<int:pk>/amenities", RoomAmenities.as_view()),
    path("amenities/", Amenities.as_view()),
    path("amenities/<int:pk>/", AmenityDetail.as_view()),
]
