from random import randint
a = randint(1, 100)
while True:
    b = int(input("угадайте число от 1 до 100:"))
    if b > a: print("Меньше")
    elif b < a: print("Больше")
    else: print("Угадал!"); break
