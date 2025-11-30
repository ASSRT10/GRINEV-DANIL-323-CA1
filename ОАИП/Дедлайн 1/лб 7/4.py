a = int(input("введите високостный год"))
print("Да" if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0) else "Нет")