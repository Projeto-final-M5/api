from django.test import TestCase
from uuid import uuid4

from users.models import User
from users.tests.mocks import mock_user


class FeedBackModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.
