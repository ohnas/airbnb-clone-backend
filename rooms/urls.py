from django.urls import path
from rooms.views import see_one_room, see_all_room

urlpatterns = [
    path("", see_all_room),
    path("<int:room_pk>/", see_one_room),
]
