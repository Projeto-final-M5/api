from django.urls import reverse

from rest_framework.test import APITestCase

from extra_datas.models import Extra_Data
from users.models import User
from users.tests.mocks import mock_user, mock_diff, mock_user_login

from books.models import Book
from .mocks import mock_book, mock_extra_data, mock_genders


class BookViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = mock_user

        cls.book_data = mock_book
        cls.extra_data_data = mock_extra_data
        cls.gender_data = mock_genders

        cls.user = User.objects.create_user(**cls.user_data)
        cls.user_login = mock_user_login

        cls.base_url_user = reverse("users")
        cls.login = reverse("login")
        cls.base_url = reverse("book")

    def test_can_create_book(self):
        user_token = self.client.post(self.login, self.user_login, format="json")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + user_token.data["token"])

        response = self.client.post(
            self.base_url,
            {
                **self.book_data,
                "user": self.user_data,
                "extra_data": self.extra_data_data,
                "genders": self.gender_data,
            },
            format="json",
        )

        data = {
            **response.data,
            **self.book_data,
            "price": "20.00",
        }

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, data)

    def test_cant_create_book_with_wrong_keys(self):
        user_token = self.client.post(self.login, self.user_login, format="json")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + user_token.data["token"])

        response = self.client.post(
            self.base_url,
            {
                "title": "Don Quixote",
            },
            format="json",
        )

        data = {
            "author": ["This field is required."],
            "year": ["This field is required."],
            "price": ["This field is required."],
            "publishing": ["This field is required."],
            "condition": ["This field is required."],
            "isbn": ["This field is required."],
        }

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, data)

    def test_cant_create_book_without_authentication(self):
        response = self.client.post(
            self.base_url,
            {
                **self.book_data,
                "extra_data": self.extra_data_data,
                "user": self.user_data,
            },
            format="json",
        )

        data = {"detail": "Authentication credentials were not provided."}

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, data)
