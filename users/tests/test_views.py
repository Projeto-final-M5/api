from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from .mock import (
    mock_user,
    mock_adm_post,
    mock_user_post,
    mock_adm_login,
    mock_user_login,
)


class UserViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.adm_data = mock_adm_post
        cls.user_data = mock_user_post
        cls.user_wrong_data = mock_user

        cls.adm_login = mock_adm_login
        cls.user_login = mock_user_login

        cls.base_url = reverse("users")
        cls.login = reverse("login")

    def test_can_create_user(self):
        response = self.client.post(self.base_url, self.user_data, format="json")

        user = {
            "id": response.data["id"],
            "username": self.user_data["username"],
            "email": self.user_data["email"],
            "birth": self.user_data["birth"],
            "is_active": True,
            "avatar": None,
            "stars": 5,
            "date_joined": response.data["date_joined"],
        }

        address = {
            "id": response.data["address"]["id"],
            "state": response.data["address"]["state"],
            "city": response.data["address"]["city"],
            "district": self.user_data["address"]["district"],
            "place": response.data["address"]["place"],
            "zip_code": self.user_data["address"]["zip_code"],
            "number": self.user_data["address"]["number"],
            "additional_data": self.user_data["address"]["additional_data"],
            "user": response.data["address"]["user"],
        }

        data = {**user, "address": address}

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, data)

    def test_cant_create_user_with_same_username(self):
        self.client.post(self.base_url, self.user_data, format="json")
        response = self.client.post(self.base_url, self.user_data, format="json")

        data = {"username": ["A user with that username already exists."]}

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, data)

    def test_cant_create_user_with_wrong_keys(self):
        response = self.client.post(
            self.base_url, {**self.user_wrong_data, "address": {}}, format="json"
        )

        data = {
            "district": ["This field is required."],
            "number": ["This field is required."],
            "zip_code": ["This field is required."],
        }

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, data)