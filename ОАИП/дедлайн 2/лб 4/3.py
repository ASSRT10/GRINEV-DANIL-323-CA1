tasks = []
while True:
    print("\n1 - Показать все задачи\n2 - Добавить задачу\n3 - Удалить задачу\n4 - Выйти")
    choice = input("Выберите действие: ")
    if choice == '1':
        if tasks:
            print("Ваши задачи:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("Задач нет")
    elif choice == '2':
        task = input("Введите задачу: ")
        tasks.append(task)
        print(f"Задача '{task}' добавлена")
    elif choice == '3':
        if tasks:
            print("Ваши задачи:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            num = int(input("Какую задачу выполнили? ")) - 1
            if 0 <= num < len(tasks):
                removed = tasks.pop(num)
                print(f"Задача '{removed}' удалена!")
            else:
                print("Неверный номер")
        else:
            print("Задач нет")
    elif choice == '4':
        break