import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector, books_list):
        # добавляем две книги
        collector.add_new_book(books_list[0])
        collector.add_new_book(books_list[1])

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_same_book(self, collector, books_list):
        collector.add_new_book(books_list[0])
        collector.add_new_book(books_list[0])

        assert len(collector.get_books_rating()) == 1
    
    def test_set_book_rating_rate_book_not_in_list(self, collector, books_list):
        collector.set_book_rating(books_list[0], 2)
        
        assert collector.get_book_rating(books_list[0]) == None

    def test_set_book_raiting_set_rating_less_than_one(self, collector, books_list):
        collector.add_new_book(books_list[0])
        collector.set_book_rating(books_list[0], 0)

        assert collector.get_book_rating(books_list[0]) == 1

    def test_set_book_raiting_set_rating_more_than_ten(self, collector, books_list):
        collector.add_new_book(books_list[0])
        collector.set_book_rating(books_list[0], 11)

        assert collector.get_book_rating(books_list[0]) == 1

    def test_get_book_raiting_get_rating_of_missing_book(self, collector, books_list):

        assert collector.get_book_rating(books_list[0]) == None
    
    def test_add_book_in_favorites_add_two_books(self, collector, books_list):
        collector.add_new_book(books_list[0])
        collector.add_new_book(books_list[1])
        collector.add_book_in_favorites(books_list[0])
        collector.add_book_in_favorites(books_list[1])

        assert len(collector.get_list_of_favorites_books()) == 2

    def test_add_book_in_favorites_add_book_not_from_books_rating(self, collector, books_list):
        collector.add_new_book(books_list[0])
        collector.add_new_book(books_list[1])
        collector.add_book_in_favorites(books_list[2])

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_delete_book(self, collector, books_list):
        collector.add_new_book(books_list[0])
        collector.add_book_in_favorites(books_list[0])
        collector.delete_book_from_favorites(books_list[0])

        assert len(collector.get_list_of_favorites_books()) == 0

# Проверка добавления книг. +
# Нельзя добавить одну и ту же книгу дважды. +
# Нельзя выставить рейтинг книге, которой нет в списке. +
# Нельзя выставить рейтинг меньше 1. +
# Нельзя выставить рейтинг больше 10. +
# У не добавленной книги нет рейтинга. +
# Добавление книги в избранное. +
# Нельзя добавить книгу в избранное, если её нет в словаре books_rating. +
# Проверка удаления книги из избранного. +

# Ожидаемы результат в имени тестов?