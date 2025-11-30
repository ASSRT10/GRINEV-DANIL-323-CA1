a = int(input("введите число: "))
for b in range(1, a + 1):
    for c in range(1, b + 1):
        print(c, end='')
    for c in range(b - 1, 0, -1):
        print(c, end='')
    print()
