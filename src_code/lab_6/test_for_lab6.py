import pytest
from code_of_lab5 import BookShop, Book
from code_of_lab5 import Book, BookShop  

@pytest.fixture
def bookshop_with_books():
    shop = BookShop()
    book1 = Book("Притулок", 350, "Меделін Ру", 50, 100)
    book2 = Book("Учень убивці", 200, "Робін Гобб", 30, 80)
    book3 = Book("Машина", 500, "Дарія Піскозуб", 40, 120)
    shop.add_book(book1, book2, book3)                                                         
    return shop

def test_add_book(bookshop_with_books):
    assert len(bookshop_with_books.books) == 3

def test_remove_new_book(bookshop_with_books):
    new_book = Book(title="Test Book", price=10,author="Test Author", quantity=5, number_of_sales=0)
    bookshop_with_books.add_book(new_book)
    bookshop_with_books.remove_book("Test Book")
    assert len(bookshop_with_books.books) == 3

def test_remove_existing_book(bookshop_with_books):
    bookshop_with_books.remove_book("Машина")
    assert len(bookshop_with_books.books) == 2

def test_remove_book_from_empty_shop():
    empty_shop = BookShop()
    empty_shop.remove_book("Non-existing Book")
    assert len(empty_shop.books) == 0

def test_remove_non_existing_book(bookshop_with_books):
    bookshop_with_books.remove_book("Non-existing Book")
    assert len(bookshop_with_books.books) == 3

def test_top_books_by_price(bookshop_with_books):
    top_books_by_price = bookshop_with_books.sort_top_books_by_price(3)
    assert len(top_books_by_price) == 3
    assert top_books_by_price[0].price <= top_books_by_price[1].price <= top_books_by_price[2].price

def test_top_books_by_sales(bookshop_with_books):
    top_books_by_sales = bookshop_with_books.sort_top_books_by_sales(3)
    assert len(top_books_by_sales) == 3
    assert top_books_by_sales[0].number_of_sales >= top_books_by_sales[1].number_of_sales >= top_books_by_sales[2].number_of_sales

