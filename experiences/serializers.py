from rest_framework.serializers import ModelSerializer
from experiences.models import Perk
from experiences.models import Experience
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"


class ExperienceDetailSeralizer(ModelSerializer):

    host = TinyUserSerializer(read_only=True)
    perks = PerkSerializer(
        read_only=True,
        many=True,
    )
    category = CategorySerializer(
        read_only=True,
    )

    class Meta:
        model = Experience
        fields = "__all__"


class ExperienceListSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = (
            "pk",
            "country",
            "city",
            "name",
            "price",
        )
