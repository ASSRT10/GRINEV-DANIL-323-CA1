d = input("Введите дату (дд.мм.гггг): ")
if len(d) == 10 and d[2] == '.' and d[5] == '.':
    a = d[:2]
    b = d[3:5]
    c = d[6:]
    if a.isdigit() and b.isdigit() and c.isdigit():
        x = int(a)
        y = int(b)
        z = int(c)
        if 1900 <= z <= 2025:
            if 1 <= y <= 12:
                if y in [1, 3, 5, 7, 8, 10, 12]:
                    m = 31
                elif y in [4, 6, 9, 11]:
                    m = 30
                elif y == 2:
                    if (z % 4 == 0 and z % 100 != 0) or (z % 400 == 0):
                        m = 29
                    else:
                        m = 28
                if 1 <= x <= m:
                    print("Корректно")
                else:
                    print("Ошибка")
            else:
                print("Ошибка")
        else:
            print("Ошибка")
    else:
        print("Ошибка")
else:
    print("Ошибка")