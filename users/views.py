from rest_framework.generics import ListCreateAPIView

from .models import User
from .serializers import UserPostSerializer

from addresses.models import Address


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserPostSerializer

    def perform_create(self, serializer):
        address = self.request.data.pop("address")
        user = serializer.save()
        Address.objects.create(**address, user=user)
