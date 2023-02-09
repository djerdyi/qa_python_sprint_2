import pytest

from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()

    return collector

@pytest.fixture(scope='session')
def book_dict():
    book_dict = {
        'Человек, который принял жену за шляпу': 2,
        'Мой дедушка был вишней': 4,
        'Давайте все убьём Констанцию': 4,
        'Как я стал идиотом': 7,
        'НИ СЫ': 7,
        'С пингвином в рюкзаке': 10
    }

    return book_dict

@pytest.fixture(scope='session')
def book_list(book_dict):
    book_list = list(book_dict.keys())

    return book_list
