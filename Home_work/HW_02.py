# 1.
# h = int(input("Enter HP: "))
# if h <= 0:
#     print("False")
# else:
#     print("True")

# 1.1 Ternarnyi operatop
# hp = int(input("Enter HP: "))
# print(False if hp <= 0 else True)

# 2.
# num = int(input("Enter number: "))
# if num % 2 == 0:
#     print("Четное")
# else:
#     print("Не четное")

# 3.
# year = int(input("Enter year:  "))
# if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
#     print(f"{year} - leap year")
# else:
#     print(f"{year} - NO leap year")

# 4.
# text = input("Enter txt: ")
# count = int(input("Enter count: "))
# for i in range(count):
#     print(text)

# 5.
# num1 = int(input("Enter number1: "))
# operator = input("Enter operator: ")
# num2 = int(input("Enter number2: "))
# =====
# if operator == "/":
#     print(round(num1 / num2))
# elif operator == "*":
#     print(num1 * num2)
# elif operator == '+':
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# =========
# if operator == "/":
#     result = round(num1 / num2)
# elif operator == "*":
#     result = num1 * num2
# elif operator == '+':
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# else:
#     print("Operator not found")
# print(f"{num1} {operator} {num2} = {result}")
#
# def health_value():
#     live = 100
#     while live >= 0:
#         damage = int(input("Please enter damage value: "))
#         if live - damage >= 0:
#             print("Alive")
#             live = live - damage
#             print(live)
#         else:
#             print("Dead")
#             break