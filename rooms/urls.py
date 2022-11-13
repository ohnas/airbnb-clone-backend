from django.urls import path
from rooms.views import see_all_room, see_one_room

urlpatterns = [
    path("", see_all_room),
    path("<int:room_id>/", see_one_room),
]
