from rest_framework import serializers
from borroweds.models import Borrowed


class BorrowedsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Borrowed
        fields = [
            "id",
            "initial_date",
            "finish_date",
            "shipping_method",
            "user_id",
            "book_id",
        ]
        read_only_fields = [
            "id",
            "initial_date",
            "user_id",
            "book_id"
        ]
