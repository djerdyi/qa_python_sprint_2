# qa_python_sprint_2

### Фикстуры
1. **collector** - создаёт и возвращает экземпляр класса BooksCollector, вызывается перед каждым тестом.
2. **book_dict** - создаёт и возвразает словрь с валидными данными для тестирования (ключи - названия книг, значения - рейтинг), вызывается один раз перед запуском всех тестов.
3. **book_list** - возвращает список ключей из book_dict (так удобнее работать с тестовыми данными, так как словарь с рейтингами нужен в паре тестов), вызывается один раз перед запуском всех тестов.

### Тесты
1. *test_init_empty_list_and_dict(self)*
    * Входные параметры: нет.
    * Что проверяем: создание экземпляра класса BooksCollector.
    * Какой ждём результат: в новом объекте содаётся пустой словарь books_rating и пустой список favorites.
2. *test_get_books_rating_get_book_list(self, collector, book_dict)*
    * Входные параметры: объёкт класса BooksCollector, словарь с тестовыми данными book_dict.
    * Что проверяем: метод `get_books_rating` возвращает нужный словарь книг.
    * Как проверяем: записываем в переменную объекта словарь с тестовыми данными.
    * Какой ждём результат: метод вернул тот же словарь, который был передан в переменную.
3. *test_add_new_book_add_two_books(self, collector, book_list)*
    * Входные параметры: объёкт класса BooksCollector, список с тестовыми данными book_list.
    * Что проверяем: добавление двух книг.
    * Какой ждём результат: кол-во элементов в возвращённом списке == кол-ву добавленных книг.
4. *test_add_new_book_add_same_book(self, collector, book_list)*
    * Входные параметры: объёкт класса BooksCollector, список с тестовыми данными book_list.
    * Что проверяем: добавление одной и той же книги.
    * Какой ждём результат: после повторного добавление такой же книги кол-во элементов в возвращённом списке == 1.
5. *test_get_book_rating_get_default_rating_by_book_name(self, collector, book_list)*
    * Входные параметры: объёкт класса BooksCollector, список с тестовыми данными book_list.
    * Что проверяем: установку рейтинга по умолчанию.
    * Какой ждём результат: рейтинг по умолчанию == 1.
6. *test_get_book_rating_get_rating_by_book_name(self, collector, book_list)*
    * Входные параметры: объёкт класса BooksCollector, список с тестовыми данными book_list.
    * Что проверяем: установку рейтинга доабавленной книге.
    * Какой ждём результат: метод `get_book_rating` вернул тот же рейтинг, который задали вручную в тесте.
7. *test_set_book_rating_rate_book_not_in_list(self, collector, book_list)*
    * Входные параметры: объёкт класса BooksCollector, список с тестовыми данными book_list.
    * Что проверяем: получение рейтинга книги, которой нет в списке.
    * Какой ждём результат: рейтинг не установлен, метод `get_book_rating` вернул `None`.
8. *test_set_book_rating_set_rating_less_than_one(self, collector, book_list)*
    * Входные параметры: объёкт класса BooksCollector, список с тестовыми данными book_list.
    * Что проверяем: нельза задать рейтинг < 1.
    * Какой ждём результат: рейтинг не изменился, на выходе `get_book_rating` получили дефолтное значение.
9. *test_set_book_rating_set_rating_more_than_ten(self, collector, book_list)*
    * Входные параметры: объёкт класса BooksCollector, список с тестовыми данными book_list.
    * Что проверяем: нельзя задать рейтинг > 10.
    * Какой ждём результат: рейтинг не изменился, на выходе `get_book_rating` получили дефолтное значение.
10. *test_get_book_rating_get_rating_of_missing_book(self, collector, book_list)*
    * Входные параметры: объёкт класса BooksCollector, список с тестовыми данными book_list.
    * Что проверяем: у не добавленной книги нет рейтинга.
    * Какой ждём результат: рейтинг не установлен, метод `get_book_rating` вернул `None`.
11. *test_get_books_with_specific_rating_get_book_by_rating(self, collector, book_list, book_dict)*
    * Входные параметры: объёкт класса BooksCollector, список с тестовыми данными book_list и словарь с тестовыми данными book_dict.
    * Что проверяем: получение списка книг по указанному рейтингу.
    * Как проверяем: записываем в переменную объекта словарь с тестовыми данными -> берём случайную книгу из тестового словаря -> считаем, кол-во книг с таким же рейтингом.
    * Какой ждём результат: метод `get_books_with_specific_rating` вернул такое же кол-во книг, какое получилось у при подсчёте.
12. *test_add_book_in_favorites_add_two_books(self, collector, book_list)*
    * Входные параметры: объёкт класса BooksCollector, список с тестовыми данными book_list.
    * Что проверяем: добавление двух книг в избранное.
    * Какой ждём результат: кол-во элементов списка избранного == 2.
13. *test_add_book_in_favorites_add_same_book_to_favorites(self, collector, book_list)*
    * Входные параметры: объёкт класса BooksCollector, список с тестовыми данными book_list.
    * Что проверяем: добавление одной и той же книги в избранное.
    * Какой ждём результат: кол-во элементов списка избранного == 1.
14. *test_add_book_in_favorites_add_book_not_from_books_rating(self, collector, book_list)*
    * Входные параметры: объёкт класса BooksCollector, список с тестовыми данными book_list.
    * Что проверяем: нельзя добавить книгу в избранное, если её нет в основном списке.
    * Какой ждём результат: метод `get_list_of_favorites_books` вернул пустой список.
15. *test_delete_book_from_favorites_delete_book(self, collector, book_list)*
    * Входные параметры: объёкт класса BooksCollector, список с тестовыми данными book_list.
    * Что проверяем: удаление книги из избранного.
    * Как проверяем: добавляем книгу в общий список -> добавлем эту же книгу в избранное -> удаляем эту же книгу из избранного.
    * Какой ждём результат: метод `get_list_of_favorites_books` вернул пустой список.
