import pytest
import random

from main import BooksCollector

# Класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    # Проверяем __init__
    def test_init_empty_list_and_dict(self):
        collector = BooksCollector()

        assert collector.books_rating == {} and collector.favorites == []
    
    # Проверяем, что метод возвращает нужный словарь книг
    def test_get_books_rating_get_book_list(self, collector, book_dict):
        collector.books_rating = book_dict

        assert collector.get_books_rating() == book_dict

    # Проверяем добавление двух книг
    def test_add_new_book_add_two_books(self, collector, book_list):
        collector.add_new_book(book_list[0])
        collector.add_new_book(book_list[1])

        assert len(collector.get_books_rating()) == 2

    # Проверяем добавление одной и той же книги
    def test_add_new_book_add_same_book(self, collector, book_list):
        collector.add_new_book(book_list[0])
        collector.add_new_book(book_list[0])

        assert len(collector.get_books_rating()) == 1

    # Проверяем дефолтный рейтинг доабавленной книги
    def test_get_book_rating_get_default_rating_by_book_name(self, collector, book_list):
        collector.add_new_book(book_list[0])
        
        assert collector.get_book_rating(book_list[0]) == 1

    # Проверяем установку рейтинга доабавленной книге
    def test_get_book_rating_get_rating_by_book_name(self, collector, book_list):
        collector.add_new_book(book_list[0])
        collector.set_book_rating(book_list[0], 7)
        
        assert collector.get_book_rating(book_list[0]) == 7

    # Проверяем получение рейтинга книги, которой нет в списке
    def test_set_book_rating_rate_book_not_in_list(self, collector, book_list):
        collector.set_book_rating(book_list[0], 2)
        
        assert collector.get_book_rating(book_list[0]) == None

    # Проверяем, что нельза задать рейтинг < 1
    def test_set_book_rating_set_rating_less_than_one(self, collector, book_list):
        collector.add_new_book(book_list[0])
        collector.set_book_rating(book_list[0], 0)

        assert collector.get_book_rating(book_list[0]) == 1

    # Проверяем, что нельзя задать рейтинг > 10
    def test_set_book_rating_set_rating_more_than_ten(self, collector, book_list):
        collector.add_new_book(book_list[0])
        collector.set_book_rating(book_list[0], 11)

        assert collector.get_book_rating(book_list[0]) == 1
    
    # Проверяем, что у не добавленной книги нет рейтинга
    def test_get_book_rating_get_rating_of_missing_book(self, collector, book_list):

        assert collector.get_book_rating(book_list[0]) == None
    
    # Проверяем получение списка книг по указанному рейтингу
    def test_get_books_with_specific_rating_get_book_by_rating(self, collector, book_list, book_dict):
        collector.books_rating = book_dict
        random_book_number_in_list = random.randint(0, len(book_list) - 1)
        rating = book_dict.get(book_list[random_book_number_in_list])
        count_books_with_rating = 0
        for value in book_dict.values():
            if value == rating:
                count_books_with_rating += 1
                
        assert len(collector.get_books_with_specific_rating(rating)) == count_books_with_rating
    
    # Проверяем добавление двух книг в избранное
    def test_add_book_in_favorites_add_two_books(self, collector, book_list):
        collector.add_new_book(book_list[0])
        collector.add_new_book(book_list[1])
        collector.add_book_in_favorites(book_list[0])
        collector.add_book_in_favorites(book_list[1])

        assert len(collector.get_list_of_favorites_books()) == 2

    # Проверяем добавление одной и той же книги в избранное
    def test_add_book_in_favorites_add_same_book_to_favorites(self, collector, book_list):
        collector.add_new_book(book_list[0])
        collector.add_book_in_favorites(book_list[0])
        collector.add_book_in_favorites(book_list[0])

        assert len(collector.get_list_of_favorites_books()) == 1

    # Проверяем, что нельзя добавить книгу в избранное, если её нет в основном списке
    def test_add_book_in_favorites_add_book_not_from_books_rating(self, collector, book_list):
        collector.add_new_book(book_list[0])
        collector.add_book_in_favorites(book_list[1])

        assert collector.get_list_of_favorites_books() == []
    
    # Проверяем удаление книги из избранного
    def test_delete_book_from_favorites_delete_book(self, collector, book_list):
        collector.add_new_book(book_list[0])
        collector.add_book_in_favorites(book_list[0])
        collector.delete_book_from_favorites(book_list[0])

        assert collector.get_list_of_favorites_books() == []
