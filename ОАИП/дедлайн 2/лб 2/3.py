a = input("введите текст:")
b = c = d = i = 0
for c in a:
    if c.isalpha(): b += 1
    elif c.isdigit(): c += 1
    elif c in '.,!?:;': d += 1
    elif c == ' ': i += 1
print(f"букв = {b}")
print(f"цифр = {c}")
print(f"знаков препинания = {d}")
print(f"пробелов = {i}")
