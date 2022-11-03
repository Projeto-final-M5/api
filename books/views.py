from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import Response, status
from django.shortcuts import get_object_or_404

from .models import  Book
from .serializers import BookPostSerializer, BookGetUpdateSerializer
from genders.models import Gender
from users.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from extra_datas.models import Extra_Data

# Create your views here.
class BookView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookPostSerializer

    def perform_create(self, serializer):

        genders = self.request.data.pop('genders')

        extra = self.request.data.pop('extra_data')
        
        book = serializer.save(user=self.request.user)

        Extra_Data.objects.create(**extra, books=book)

        for item in genders:
            gender , _ = Gender.objects.get_or_create(**item)        
            gender.books.add(book)

class BookGetIdView(RetrieveUpdateAPIView):

    authentication_classes = [TokenAuthentication]
    
    queryset = Book.objects.all()
    serializer_class = BookPostSerializer

    