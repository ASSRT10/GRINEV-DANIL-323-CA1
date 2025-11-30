a = ""
while True:
    b = input("введите данные")
    if b == "":
        break
    a += b + " "
words = a.lower().split()
c = {}
for d in words:
    d = d.strip('.,!?;:')
    c[d] = c.get(d, 0) + 1
print(f"Статистика слов: {c}")
