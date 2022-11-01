from rest_framework import serializers

from borroweds.serializers import BorrowedsSerializers
from extra_datas.serializers import Extra_DataSerializer
from genders.serializers import GenderSerializer

from books.models import Book


class BookPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "transaction",
            "available",
            "author",
            "price",
            "language",
            "edition",
            "condition",
            "isbn",
            # "extra_data",
            "genders",
        ]

        extra_kwargs = {"id": {"read_only": True}}

        extra_data = Extra_DataSerializer(many=True)
        genders = GenderSerializer(many=True)


class BookGetUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "transaction",
            "available",
            "author",
            "price",
            "language",
            "edition",
            "condition",
            "isbn",
            # "extra_data",
            "genders",
            # "borrowed",
        ]

        extra_kwargs = {"id": {"read_only": True}, "condition": {"read_only": True}}

        extra_data = Extra_DataSerializer(many=True)
        genders = GenderSerializer(many=True)
        borrowed = BorrowedsSerializers(many=True)
