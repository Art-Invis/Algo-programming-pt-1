"""
Module with classes for representing books and bookshops.
"""

class Book:
    """
    Represents a book with various attributes.

    Attributes:
    - title (str): The title of the book.
    - price (float): The price of the book in Ukrainian hryvnia.
    - author (str): The author of the book.
    - quantity (int): The quantity of the book available in the bookshop.
    - number_of_sales (int): The number of sales for the book.

    Methods:
    - display_info(): Displays information about the book.
    """
    # Приглушення повідомлення pylint про занадто мало публічних методів

    def __init__(self, title, price, author, quantity, number_of_sales):
        """
        Initializes a Book instance with the given attributes.

        Parameters:
        - title (str): The title of the book.
        - price (float): The price of the book in Ukrainian hryvnia.
        - author (str): The author of the book.
        - quantity (int): The quantity of the book available in the bookshop.
        - number_of_sales (int): The number of sales for the book.
        """
        self.title = title
        self.price = price
        self.author = author
        self.quantity = quantity
        self.number_of_sales = number_of_sales

    def display_info(self):
        """
        Displays information about the book.
        """
        print(f"Назва книжки: {self.title}")
        print(f"Ціна: {self.price} грн")
        print(f"Автор: {self.author}")
        print(f"К-сть на складі: {self.quantity}")
        print(f"К-сть продажів: {self.number_of_sales}")
        print("\n")



class BookShop:
    """
    Represents a bookshop with a collection of books.

    Attributes:
    - books (list): A list containing instances of Book.

    Methods:
    - add_book(book): Adds a book to the bookshop.
    - remove_book(title): Removes a book from the bookshop by title.
    - display_top_books_by_price(n): Displays the top n books by price.
    - display_top_books_by_sales(n): Displays the top n books by sales.
    """

    def __init__(self):
        """
        Initializes a BookShop instance with an empty list of books.
        """
        self.books = []

    def add_book(self, *books):
        """
        Adds a book to the bookshop.

        Parameters:
        - book (Book): The Book instance to be added.
        """
        self.books.extend(books)

    def remove_book(self, title):
        """
        Removes a book from the bookshop by title.

        Parameters:
        - title (str): The title of the book to be removed.
        """
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"{title} була видалена з магазину.\n")
                return
        print(f"Книжка під назвою {title} не знайдена на складі.")

    def sort_top_books_by_price(self, n):
        """
        Sort the top n books by price.

        Parameters:
        - n (int): The number of top books to sort.
        """
        sorted_books = sorted(self.books, key=lambda x: x.price, reverse=False)[:n]
        return sorted_books

    def display_top_books_by_price(self, n):
        """
        Displays the top n books by price.

        Parameters:
        - n (int): The number of top books to display.
        """
        sorted_books = sorted(self.books, key=lambda x: x.price, reverse=False)[:n]
        print(f"Топ-{n} книжок за ціною:")

        for book in sorted_books:
            book.display_info()

    def sort_top_books_by_sales(self, n):
        """
        Sort the top n books by sales.

        Parameters:
        - n (int): The number of top books to sort.
        """
        sorted_books = sorted(self.books, key=lambda x: x.number_of_sales, reverse=True)[:n]
        return sorted_books

    def display_top_books_by_sales(self, n):
        """
        Displays the top n books by sales.

        Parameters:
        - n (int): The number of top books to display.
        """
        sorted_books = sorted(self.books, key=lambda x: x.number_of_sales, reverse=True)[:n]

        print(f"Топ-{n} книжок за продажами:")
        for book in sorted_books:
            book.display_info()

def main():
    """
    Example usage of the Book and BookShop classes.
    """
    book1 = Book("Притулок", 350, "Меделін Ру", 50, 100)
    book2 = Book("Учень убивці", 200, "Робін Гобб", 30, 80)
    book3 = Book("Машина", 500, "Дарія Піскозуб", 40, 120)

    bookshop = BookShop()
    bookshop.add_book(book1, book2, book3)

    print("Початковий склад книжок:\n")
    for book in bookshop.books:
        book.display_info()

    bookshop.display_top_books_by_price(3)
    bookshop.display_top_books_by_sales(3)

    bookshop.remove_book("Машина")

    print("Оновлений склад книжок:\n")
    for book in bookshop.books:
        book.display_info()

main()
