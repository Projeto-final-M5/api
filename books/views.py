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
from utils.validation_error import CustomForbidenError
from extra_datas.serializers import Extra_DataSerializer
from genders.serializers import GenderSerializer,GenderSerializerChoices


# Create your views here.
class BookView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookPostSerializer

    def perform_create(self, serializer):
        if "genders" not in self.request.data.keys():
            raise CustomForbidenError({"genders":["This camp is required."]})
        
        if "extra_data" not in self.request.data.keys():
            raise CustomForbidenError({"extra_data":["This camp is required."]})

        book = serializer.save(user=self.request.user)

        
    
        
        extra = self.request.data.pop("extra_data")

        extraSerializer = Extra_DataSerializer(data=extra)
        extraSerializer.is_valid(raise_exception=True)
        
        Extra_Data.objects.create(**extra,book=book)
        
        genders = self.request.data.pop("genders")

        genderSerializer = GenderSerializer
        for item in genders:
            genderSerializer = GenderSerializer(data=item)
            genderSerializer.is_valid(raise_exception=True)
            
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
    
    def get_serializer(self, *args, **kwargs):
        book = self.get_object()
        print(book)

        if "extra_data" in self.request.data.keys():
            extra = self.request.data.pop("extra_data")
            Extra_Data.objects.update(**extra)

        if "genders" in self.request.data.keys():
            genders = self.request.data.pop("genders")
            book.genders.clear()

            for item in genders:
                gender, _ = Gender.objects.get_or_create(**item)
                book.genders.add(gender)

        return super().get_serializer(*args, **kwargs)

class BookDeleteView(UpdateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdmOrOwnerBook]

    queryset = Book.objects.all()
    serializer_class = BookDeleteSerializer

