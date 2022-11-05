from rest_framework import serializers
from borroweds.serializers import BorrowedsSerializers

from feed_back.models import FeedBack


class PostFeedBackSerializers(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = [
            "id",
            "borrowed",
            "stars_owner",
            "stars_renter",
            "rating_owner",
            "rating_renter",
        ]
        borrowed = BorrowedsSerializers()


class GetOrUpdateFeedBackSerializers(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = [
            "id",
            "borrowed",
            "stars_owner",
            "stars_renter",
            "rating_owner",
            "rating_renter",
        ]
        borrowed = BorrowedsSerializers()
