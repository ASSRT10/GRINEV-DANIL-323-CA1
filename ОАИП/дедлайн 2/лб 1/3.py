a = input("введите любые слова").lower().replace(' ', '')
b, c = 0, len(a) - 1
while b < c:
    if a[b] != a[c]:
        print("Нет, это не палиндром")
        break
    b += 1
    c -= 1
else:
    print("Да, это палиндром")
