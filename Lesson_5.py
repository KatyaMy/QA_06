# SELF  ссылка на экземпляр класса
# (self является важным параметром методов класса в Python,
# который позволяет им работать с атрибутами и методами экземпляров класса.)
class Dog:
    b_class = 'Animal'

    # статический
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    # dinamic
    def run(self):
        return 'I can run!'

    def get_name(self):
        return f'Hi. My name is {self.name}'

    def set_name(self, new_name):
        self.name = new_name


dog1 = Dog('Ax', 5, 'Brown')
# print(f'Name: {dog1.name}')
# print(dog1.color)
# print(dog1.weight)
print(dog1.get_name())
# print(dog1.run())
# print(dog1.b_class)

dog2 = Dog('Missi', 3, 'Black')
print(dog2.get_name())
# print(dog2.b_class)
# print(dog2.color)
# print(dog2.__dict__)

dog2.name = 'Koll'
print(dog2.get_name())

print(dog2.set_name('Gurr'))


class Pitbull(Dog):
    def __init__(self, name, weight, color, passport):
        super().__init__(name, weight, color)
        self.passport = passport

    def give_a_paw(self):
        return 'I can give a paw!'

    def run(self):
        return 'I can run faster!!!'


# Создаем Объект класса Pitbull
dog3 = Pitbull('Flaffy', 8, 'Red', 'type1')
print(dog3.get_name())
# print(dog3.give_a_paw())
# print(dog3.passport)
# print(dog2.passport)
# print(dog2.run())
# print(dog3.run())


