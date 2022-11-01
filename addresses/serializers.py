from rest_framework import serializers

from .models import Address, AddressState, AddressCity, AddressPlace


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address

        fields = "__all__"

        extra_kwargs = {
            "id": {
                "read_only": True,
            },
        }
        