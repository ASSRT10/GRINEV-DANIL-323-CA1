a = input("введите пароль")
b = input("подтвердите пароль повторно")
if a == b:
    print("Access" if b == a else "Denied")
else:
    print("Error")