# for i in range(50):
#     print('Hello')

rows = 5
for i in range(rows +1, 1, -1):
    for i in range(0, i-1):
        print("*", end=" ")
    print(" ")
