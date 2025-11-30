a= {'Анна': '123', 'Борис': '456', 'Виктор': '789'}

while True:
    print("\n1 - Показать контакты\n2 - Добавить контакт\n3 - Удалить контакт\n4 - Выйти")
    b = input("Выберите действие: ")
    
    if b == '1':
        for c, d in a.items():
            print(f"{c}: {d}")
    elif b == '2':
        i = input("Имя: ")
        if i in a:
            print("Контакт уже существует")
        else:
            a[i] = input("Телефон: ")
    elif b== '3':
        i = input("Имя для удаления: ")
        if i in a:
            del a[i]
        else:
            print("Контакт не найден")
    elif b == '4':
        exit()

