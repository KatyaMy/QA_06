# 1.
my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2])
print(my_list[-2])
'''2. Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a' '''

# 2.1
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
sum = 0
for i in list_1:
    if isinstance(i, int):
        sum += i
print(sum)
# 2.2
a_strings = [i for i in list_1 if isinstance(i, str) and 'a' in i]
print(a_strings)

'''3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж'''
list = ['cat', 'dog', 'horse', 'cow']
print(tuple(list))
print(*list,)

'''4. Напишите программу, которая определяет, какая семья больше. 
1) Программа имеет два input() - например, family_1, family_2. 
2) Членов семьи нужно перечислить через запятую. 
Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')'''

family_1 = input('Enter members family_1: ')
family_2 = input('Enter members family_2: ')
if family_1 > family_2:
    print(f'Family_1: {family_1}')
if family_2 > family_1:
    print(f'family_2: {family_2}')
elif family_1 == family_2 or family_2 == family_1:
    print("Family Equal")

''' 5.Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
    о вашем любимом фильме. 
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение'''

film = {'title': '7v',
        'director': 'G.Smitt',
        'year': '2022',
        'budget': '45,000',
        'main_actor': 'Fred',
        'slogan': 'Be be'}
print(film.keys())
print(film.values())
print(film.items())

'''6. Найдите сумму всех значений в словаре'''
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
summ = 0
for i in my_dictionary.values():
    summ += i
print(summ)

'''7.Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1] '''
list_2 = [1, 2, 3, 4, 5, 3, 2, 1]
num = set(list_2)
print(num)

'''8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     - проверьте являются ли эти множества подмножествами друг друга '''

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1.intersection(set2, set1))
print(set2.difference(set1))
print(set1.difference(set2))
print(set1.issuperset(set2))
print(set2.issubset(set1))

s1 = "Ronaldo is better than Messsi"
print('Ronaldo' in s1)
print('Football' in s1)
print(sum(range(4, 10)))