numbers = [15, 42, 67, 88, 31, 54, 92, 10, 75, 23]
even_numbers = [x for x in numbers if x % 2 == 0]
greater_than_50 = [x for x in numbers if x > 50]
print(f"Исходный список: {numbers}")
print(f"Чётные числа: {even_numbers}")
print(f"Числа больше 50: {greater_than_50}")