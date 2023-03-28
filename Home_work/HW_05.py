"""Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
- как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений
этого атрибута нужно использовать методы get и set """


class Books:
    def __init__(self, title, author, public_year, price):
        self.title = title
        self.author = author
        self.public_year = public_year
        self._price = price

    def display_info(self):
        print(f'Author: {self.author} \nTitle: {self.title} \nPublication Year: {self.public_year}')

    def get_price(self):
        return f'Price = {self._price}'

    def set_price(self, new_price):
        self._price = new_price


book1 = Books('Kalambur', 'Huhu', 1999, 23.0)
book1.display_info()
print(book1.get_price())
print(book1.set_price(30.00))
print(book1.get_price())

print("___________")

book2 = Books('Tihii Don', 'M.Sholohov', 1904, 389.0)
book2.display_info()
