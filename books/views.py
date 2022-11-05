from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from rest_framework.views import Response, status
from django.shortcuts import get_object_or_404

from .models import Book
from .serializers import (
    BookPostSerializer,
    BookGetUpdateSerializer,
    BookDeleteSerializer,
)
from genders.models import Gender
from users.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from extra_datas.models import Extra_Data
from .permissions import IsAdmOrOwnerBook


# Create your views here.
class BookView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookPostSerializer

    def perform_create(self, serializer):
        genders = self.request.data.pop("genders")
        book = serializer.save(user=self.request.user)

        if "extra_data" in self.request.data.keys():
            extra = self.request.data.pop("extra_data")
            Extra_Data.objects.create(**extra, book=book)

        for item in genders:
            gender, _ = Gender.objects.get_or_create(**item)
            book.genders.add(gender)

        # for item in genders:
        #     gender, _ = Gender.objects.get_or_create(**item)
        #     gender.books.add(book)


class BookGetPacthDeleteIdView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdmOrOwnerBook]

    queryset = Book.objects.all()
    serializer_class = BookGetUpdateSerializer


class BookDeleteView(UpdateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdmOrOwnerBook]

    queryset = Book.objects.all()
    serializer_class = BookDeleteSerializer
