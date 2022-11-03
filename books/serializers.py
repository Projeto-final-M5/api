from rest_framework import serializers

from books.models import Book
from genders.serializers import GenderSerializer
from users.serializers import UserSerializer
from extra_datas.serializers import Extra_DataSerializer

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
            "publishing",
            "condition",
            "isbn",
            "genders",
            "extra_data",
            "user",
        ]
        
        extra_kwargs = {
            "id": {"read_only": True},
            "genders":{"read_only": True},
            "user":{"read_only": True},
            "extra_data":{"read_only": True},
        }
    extra_data = Extra_DataSerializer(read_only=True)

    genders = GenderSerializer(many=True,read_only=True)
        
        
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
            "publishing",
            "condition",
            "isbn",
            # "extra_data",
            "genders",
            # "borrowed",
        ]
        
        extra_kwargs = {
            "id": {"read_only": True},
            "condition": {"read_only": True},
        }
        
        # extra_data = ExtraDataSerializer(many=True)
        genders = GenderSerializer(many=True)
        # borrowed = BorrowedSerializer(many=True)