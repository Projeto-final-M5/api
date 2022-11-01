from rest_framework import serializers
from borroweds.models import Borrowed

class BorrowedsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Borrowed
        fields = ["initial_date","finish_date","shipping_method"]
        read_only_fields = ['id']

