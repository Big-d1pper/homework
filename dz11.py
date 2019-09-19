# Домашняя работа № 11 
# Описать класс «домашняя библиотека». Предусмотреть возможность работы с произвольным числом книг,
#  поиска книги по какому-либо признаку (например, по автору или по году издания),
#  добавления книг в библиотеку, удаления книг из нее, сортировки книг по разным полям.


class HomeLib(object):
    """
    This class for create lib and use some method for this books
    """
    def __init__(self, books_all):
        self.books_all = books_all

    def add_new_book(self, new_book):
        """
        For add new book
        """
        self.books_all.append(new_book)

    def search_for_name(self, name):
        """
        For search by name
        """
        for p in self.books_all:
            if p['name'] == name:
                return p

    def search_for_year(self, year):
        """
        For search by year
        """
        for p in self.books_all:
            if p['year'] == year:
                return p

    def dell_book(self, name):
        """
        For dell book
        """
        for p in self.books_all:
            if p['name'] == name:
                print(f'book {name} was deleted')
                return self.books_all.remove(p)

    def sort_by(self, param):
        """
        For sort by parametrs
        """
        sorted(self.books_all, key=lambda k: k[param])
        return self.books_all


