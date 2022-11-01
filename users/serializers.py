from rest_framework import serializers

# from borrowed.models import Borrowed
# from borrowed.serializer import BorrowedSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        exclude = [
            "first_name",
            "last_name",
            "last_login",
            "groups",
            "user_permissions",
            "is_staff",
            "is_superuser",
        ]

        extra_kwargs = {
            "id": {
                "read_only": True,
            },
            "stars": {
                "read_only": True,
            },
            "password": {
                "write_only": True,
                "required": True,
            },
            "birth": {
                "write_only": True,
                "required": True,
            },
            "email": {
                "write_only": True,
                "required": True,
            }
        }

        # borrowed = BorrowedSerializer()

    def create(self, validated_data: dict) -> dict:
        user = User.objects.create_user(**validated_data)

        return user


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        exclude = [
            "first_name",
            "last_name",
            "last_login",
            "groups",
            "user_permissions",
            "is_staff",
            "is_superuser",
        ]

        extra_kwargs = {
            "id": {
                "read_only": True,
            },
            "stars": {
                "read_only": True,
            },
            "password": {
                "write_only": True,
                "required": True,
            },
            "birth": {
                "write_only": True,
                "required": True,
            },
            "email": {
                "write_only": True,
                "required": True,
            }
        }

        # borrowed = Borrowed()

    def create(self, validated_data: dict) -> dict:
        user = User.objects.create_user(**validated_data)

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
