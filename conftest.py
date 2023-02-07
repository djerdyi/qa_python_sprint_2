import pytest

from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()

    return collector

@pytest.fixture(scope='session')
def books_list():
    books_list = [
        'Человек, который принял жену за шляпу',
        'Мой дедушка был вишней',
        'Давайте все убьём Констанцию',
        'Как я стал идиотом',
        'НИ СЫ',
        'С пингвином в рюкзаке'
    ]

    return books_list
