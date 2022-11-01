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

    
class UserPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "groups",
            "user_permissions",
            "is_superuser",
            "avatar",
            "password",
            "id",
            "last_login",
        ]
        read_only_fields = ["is_active"]


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        
        fields = "__all__"
        read_only_fields = ["id", "password", "last_login", "is_superuser", "username", "first_name", "last_name", "is_staff",
                            "date_joined", "avatar", "email", "birth", "stars", "groups", "user_permissions"
                            ]
        extra_kwargs = {
            "is_active": {'required': True},
        }

