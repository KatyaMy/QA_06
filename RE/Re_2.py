# num1 = [1, 2, 3]
# num2 = [1, 2, 3]
# num1[1] = 20
# num2[1] = 20
# print(num1)
# print(num2)

# кортеж не изменяемый, занимает меньше памяти чем лист

# lst = [1, 2, 3, 4, 5, 6]
# lst1 = (1, 2, 3, 4, 5, 6)
# print(lst.__sizeof__())
# print(lst1.__sizeof__())

#Как перевести из кортежа в лист и обратно, будет разные id
# a = (1, 2, 3)
# b = list(a)
# b[1] = 15
# c = tuple(b)
# print(a)
# print(b)
# print(c)
# print(type(a))
# print(type(b))
# print(type(c))

# num = (2, 6, 9, 1, 8)
# num1 = sorted(num)
# print(num)
# print(num1)

num = {1, 1, 3, 4, 5, 6}
print(num)
print(type(num))