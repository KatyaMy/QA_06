''' === Lists === '''

# sentence = "Python it's good"
# print(sentence.split(' ', maxsplit=2))

# my_list = [1, 'Hi', 3.4, True, None]
# print(my_list[2])
# print(my_list[-1])

# before changes a list
# print(my_list)
# print(id(my_list))

# # after change a list
# my_list[0] = 25
# print(my_list)
# print(id(my_list))

# added new list to the end
# my_list.append(sentence)
# print(my_list)
# print(len(my_list))

# my_list.insert(2, sentence)
# print(my_list)

# count how we can element whith number 1
# print(my_list.count(1))

# Number index for None
# print(my_list.index(None))

# my_list = [1, 2, 3, 4, 5, [6, 8, 33, 4, 61]]
# # print(sum(my_list))
# # print(min(my_list))
# print(my_list[-1][-2])

# my_list.reverse()
# print(my_list)
#
# num = [1,2,3,4,5]
# for numb in num:
#     print(num**2)

# new_l = [i * i for i in num if i % 2]
# print(new_l)

''' === tuples === '''

# 1. Create Tuple:
# my_tuple = 1, 2, 3
# print(my_tuple)
# print(type(my_tuple))
# 1.1 two(use round brackets)
# my_tuple = (1, 2, 3)
# print(type(my_tuple))

# my_tuple = ('apple', 'banana', 'cat')
# a, b, c = my_tuple
# print(a)
# print(b)
# print(c)

# ===How change value index at tuple, need translate into list===
# letters = list(my_tuple)
# letters[0] = 'ananas'
# print(letters)

# 2.
# my_tuple = (1, 'Name', None, 'name', 'name', 5)
# i = 0
# while i < len(my_tuple):
#     print(my_tuple[i])
#     i += 1
# 3.
# fruits = ('apple', ['ananas', 'mango'], 'melon')
# fruits[1][0] = 'cherry'
# print(fruits)

# Passing tuple as an arg in function
# def sum_it(*args):
#     total = 0
#     for num in args:
#         total = total + num
#     return total
# print(sum_it(2, 3, 4, 5, 6))

'''===Dictionary==='''
#
# my_dict = {
#     'name': 'Elena',
#     'last_name': 'Mu',
#     'age': 30,
#     'DEP': 'IT'}

# print(my_dict)
# print(my_dict['last_name'])
# my_dict['last_name'] = "Dimitrov"
# print(my_dict)
# my_dict['salary'] = 5000
# print(my_dict)
# Create a new dictionary
# empl = dict(name='Jon')
# print(empl)

'''''=====SETS====='''
# my_list = [1, 2, 3, 4, 5, 5, 6]
# my_set = {1, 'er', 55, None}
# print(set(my_list))

set1 = {1, 2, 3, 'one', 20}
set2 = {1, 2, 3, 'one', 'ten', 100, 525}
set3 = {1, 2, 3}
# print(set1.issubset(set2))
# print(set1.issuperset(set1))
# print(set1.intersection(set1))
# print(set1.difference(set2))
# print(set1.symmetric_difference(set2))

print(id(set1))
print(set1.remove(1))
print(set1.add(8))
print(set1)
