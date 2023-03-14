# s = 'hello world'
# print(s.replace(' ', ''))

# print(s.count('o'))

# w = 'Денисов Денис Денисович'
# w1 = '1, 2, 3, 4, 5'
# print(w.split())
# print(w.split('е'))
# print(w1.split(','))
# w2 = w1.split(',')
# print(''.join(w1))

# w3 = '  123hello123  '
# print(w3)
# print(w3.strip())
# print(w3.strip().strip('123'))

# w4 = 'hello world'
# # print(w4.find('e', 2, 5))
# print(w4.index('e', 2, 5))

# w5 = 'naMe? WorLd1 TiTle'
# print(w5.upper())
# print(w5.lower())
# print(w5.title())
# print(w5.capitalize())
# print(w5.swapcase())

# w6 = 'qwerty'
# w7 = 'Qwerty'
# w8 = '1234a'
# print(w6.islower())
# print(w7.islower())
# print(w8.islower())

# w6 = 'QWERTy'
# w7 = 'QWERTY'
# w8 = '1234E'
# print(w6.isupper())
# print(w7.isupper())
# print(w8.isupper())

# w6 = '01234'
# w7 = '0,1'
# w8 = '1234E'
# print(w6.isdigit())
# print(w7.isdigit())
# print(w8.isdigit())

# w6 = '01234'
# w7 = 'QWErtyu'
# w8 = '1234E'
# print(w6.isalpha())
# print(w7.isalpha())
# print(w8.isalpha())

# ===1===
# a = int(input('Enter number: '))
# if a % 2 == 0:
#     if a % 10 == 0:
#         print(f"{a} delotsy na 2 i 10")
#     else:
#         print(f"{a} delitsy na 2, No ne delitsia na 10")
# else:
#     print(f"{a} ne delitsy na 2")

# ===2===
# q = int(input("Enter you mark: "))
# if q >= 100:
#     print(5)
# elif q >= 80:
#     print(4)
# elif q >= 70:
#     print(3)
# else:
#     print(2)

# ===3===short solution
# x, y = 45, 50
# s = x if x > y else y
# print(s)

# ===4===
# value = 5
# match value:
#     case 1:
#         print(1)
#     case 2:
#         print(2)
#     case 3:
#         print(3)
#     case 4:
#         print(4)
#     case 5:
#         print(5)
#     case _:
#         print("number not faund")

# ===4===
# c = 0
# while c < 5:
#     print("Hello")
#     c += 1

# ===5===
# text = int(input("Enter number: "))
# count = 0
# while text != "stop":
#     num = int(text)
#     count += num
#     text = input("enter number or stop: ")
# print(f"Sum numb = {count}")

# ===6===
# num = 10
# for i in range(1, num+1, 2):
#     print(i)

# ===7===
# string_1 = "Hello"
# for i in range(len(string_1)):
# for i in string_1:
#     print(i)
# for i in range(len(string_1)):
#     if string_1[i].islower():
#         print(i, string_1[i])