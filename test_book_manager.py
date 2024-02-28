import unittest
from book_manager import Book, BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()
        self.book1 = Book("1234567890", "Book1", "Author1")
        self.book2 = Book("2345678901", "Book2", "Author2")
        self.book3 = Book("3456789012", "Book3", "Author3")

    def test_add_book(self):
        self.manager.add_book(self.book1)
        self.assertIn(self.book1, self.manager.list_books())

    def test_add_duplicate_book(self):
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book1)
        self.assertEqual(len(self.manager.list_books()), 1)

    def test_remove_book(self):
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book2)
        self.manager.remove_book("1234567890")
        self.assertNotIn(self.book1, self.manager.list_books())
        self.assertIn(self.book2, self.manager.list_books())

    def test_list_books(self):
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book2)
        self.manager.add_book(self.book3)
        books = self.manager.list_books()
        self.assertEqual(len(books), 3)
        self.assertIn(self.book1, books)
        self.assertIn(self.book2, books)
        self.assertIn(self.book3, books)

if __name__ == '__main__':
    unittest.main()
