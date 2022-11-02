from django.test import TestCase
from borroweds.models import Borrowed


class BorrowedModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.borrowed_data = {
            "shipping_method": "Retirada",
        }

        cls.borrowed = Borrowed.objects.create(**cls.borrowed_data)

    def test_fild_max_length(self):

        max_length = self.borrowed._meta.get_field("shipping_method").max_length
        self.assertEqual(max_length, 100)

    def test_borrowed_fields(self):
        self.assertIsNotNone(self.borrowed.id)
        self.assertEqual(
            self.borrowed.shipping_method, self.borrowed_data["shipping_method"]
        )
        self.assertIsNotNone(self.borrowed.initial_date)
        self.assertIsNone(self.borrowed.finish_date)
