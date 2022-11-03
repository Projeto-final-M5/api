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
            "number": {
                "required": True,
            },
            "zip_code": {
                "required": True,
            },
            "user": {  # REVISAR SE ISSO FAZ SENTIDO, mas será preciso para validar os testes de criação de usuário com dados inválidos do address
                "required": False,
            },
        }
