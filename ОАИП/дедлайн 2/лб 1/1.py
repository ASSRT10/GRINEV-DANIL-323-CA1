a = int(input("введите цифры"))
b = 0
while a > 0:
    b += a % 10
    a //= 10
print(b)

