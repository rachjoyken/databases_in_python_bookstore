from lib.book import Book

"""
Constructs with
id, title, author_name
"""

def test_constructs_with_fields():
    book = Book(1, "test title", "test author_name")
    assert book.id == 1
    assert book.title == "test title"
    assert book.author_name == "test author_name"

"""
We can compare two identical books
And have them be equal
"""    
def test_albums_are_equal():
    book_1 = Book(1, "test title", "test author_name")
    book_2 = Book(1, "test title", "test author_name")
    assert book_1 == book_2

"""
We can format books into a string
""" 

def test_format_books():
    book = Book(1, "test title", "test author_name")
    assert str(book) == "1 - test title - test author_name"
