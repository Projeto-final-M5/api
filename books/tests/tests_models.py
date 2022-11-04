from django.test import TestCase

from books.models import Book
from users.models import User
from extra_datas.models import Extra_Data

from users.tests.mock import mock_user


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book_data = {
            "title": "Don Quixote",
            "transaction": "Sale",
            "price": 20.00,
            "available": True,
            "author": "Miguel de Cervantes Saavedra",
            "year": "1604",
            # "edition": "Unova",
            # tirar edition, colocar publishing
            "condition": 5,
            "isbn": "9788525433633"
        }
        cls.extra_data = {
            "translated": True
        }
        cls.extra = Extra_Data.objects.create(**cls.extra_data)
        cls.user = User.objects.create(**mock_user)
        cls.book = Book.objects.create(
            **cls.book_data,
            extra_data=cls.extra,
            user=cls.user
        )

    def test_fields(self):
        self.assertEqual(
            self.book.title,
            self.book_data["title"]
        )
        self.assertEqual(
            self.book.transaction,
            self.book_data["transaction"]
        )
        self.assertEqual(
            self.book.price,
            self.book_data["price"]
        )
        self.assertEqual(
            self.book.available,
            self.book_data["available"]
        )
        self.assertEqual(
            self.book.author,
            self.book_data["author"]
        )
        self.assertEqual(
            self.book.year,
            self.book_data["year"]
        )
        # self.assertEqual( publishing
        #     self.book.edition,
        #     self.book_data["edition"]
        # )
        self.assertEqual(
            self.book.condition,
            self.book_data["condition"]
        )
        self.assertEqual(
            self.book.isbn,
            self.book_data["isbn"]
        )

    def test_book_relations(self):
        self.assertTrue(self.book.extra_data.translated)
        self.assertEqual(
            self.book.user.username,
            mock_user["username"]
        )
