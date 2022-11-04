from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .serializers import BorrowedsSerializers
from .models import Borrowed
from books.models import Book
from .permissions import isNotOwner


class BorrrowedListCreateView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, isNotOwner]

    queryset = Borrowed.objects.all()
    serializer_class = BorrowedsSerializers

    def perform_create(self, serializer):
        book_instance = get_object_or_404(Book, id=self.kwargs["pk"])

        book_instance.available = False
        book_instance.save()

        return serializer.save(book=book_instance, user=self.request.user)
