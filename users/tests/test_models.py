from datetime import date, datetime
from django.test import TestCase

from uuid import uuid4

from users.models import User

from .mock import mock_adm, mock_user


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.adm_data = mock_adm
        cls.user_data = mock_user

        # cls.borrowed_data = mock_borrowed

        cls.user = User.objects.create_user(**cls.user_data)
        cls.adm = User.objects.create_superuser(**cls.adm_data)

        # cls.borrowed = [Borrowed.objects.create(**cls.borrowed_data) for _ in range(1)]

    def test_user_model(self):
        user = User.objects.get(username="user")

        id = user._meta.get_field("id")
        username = user._meta.get_field("username")
        avatar = user._meta.get_field("avatar")
        email = user._meta.get_field("email")
        birth = user._meta.get_field("birth")
        stars = user._meta.get_field("stars")

        # borrowed = user._meta.get_field("borrowed")

        self.assertIsInstance(user, User)
        self.assertEqual(user, self.user)

        self.assertIsNotNone(id)
        self.assertEqual(id.default, uuid4)
        self.assertTrue(id.primary_key)
        self.assertFalse(id.editable)

        self.assertTrue(username.unique)
        self.assertTrue(username.max_length, 150)

        self.assertTrue(avatar.null)
        self.assertTrue(avatar.blank)
        self.assertEqual(avatar.default, None)

        self.assertFalse(email.unique)
        self.assertFalse(email.null)
        self.assertFalse(email.blank)

        self.assertFalse(birth.unique)
        self.assertFalse(birth.null)
        self.assertFalse(birth.blank)

        self.assertEqual(stars.default, 5)
        self.assertFalse(stars.editable)

        # for borrowed in self.borrowed:
        #     self.user.borrowed.add(borrowed)
            
        # self.assertEqual(len(self.borrowed), self.user.borrowed.count())
        
        # for borrowed in self.borrowed:
        #     self.assertIn(self.user, borrowed.users.all())