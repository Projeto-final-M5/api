from rest_framework import serializers

from .models import User

from addresses.serializers import AddressSerializer


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
            },
        }

    address = AddressSerializer(read_only=True)
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
                "required": True,
            },
            "email": {
                "required": True,
            },
        }

    address = AddressSerializer(read_only=True)
    # borrowed = Borrowed()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
