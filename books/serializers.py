from rest_framework import serializers

from books.models import Book
from genders.serializers import GenderSerializer

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
            "genders"
        ]
        
        extra_kwargs = {"id": {"read_only": True}}
        
        # extra_data = ExtraDataSerializer(many=True)
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
        
        extra_kwargs = {
            "id": {"read_only": True},
            "condition": {"read_only": True}
        }
        
        # extra_data = ExtraDataSerializer(many=True)
        genders = GenderSerializer(many=True)
        # borrowed = BorrowedSerializer(many=True)