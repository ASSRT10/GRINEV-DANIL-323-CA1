a = input("введите данное: ")
b = 'aeiouyаеёиоуыэюя'
c = 0
while c < len(a):
    if a[c].lower() in b:
        a = a[:c] + a[c+1:]
    else:
        c += 1
print(a)
