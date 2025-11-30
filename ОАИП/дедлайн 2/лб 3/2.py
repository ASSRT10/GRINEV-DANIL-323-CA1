a = input("введите текст").lower()
b = {}
for c in a:
    b[c] = b.get(c, 0) + 1
print(b)
