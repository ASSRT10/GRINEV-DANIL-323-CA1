a = input("введите текст")
b, c = map(int, input("введите отрезок").split())
print(a[b-1:c])