from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404

from .serializers import BorrowedsSerializers
from .models import Borrowed
from books.models import Book
from utils.validation_error import CustomForbidenError


class BorrrowedListCreateView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = []

    queryset = Borrowed.objects.all()
    serializer_class = BorrowedsSerializers

    def perform_create(self, serializer):
        book_instamce = get_object_or_404(Book, id=self.kwargs["pk"])
        if book_instamce.available is False:
            raise CustomForbidenError("This book is not available")

        book_instamce.available = False
        book_instamce.save()

        return serializer.save(book=book_instamce, user=self.request.user)
