a = int(input("Сколько чисел вы хотите ввести? "))
nums = []
for b in range(a):
    num = int(input(f"Введите число {b+1}: "))
    nums.append(num)

max_num = max(nums)
min_num = min(nums)
avg = sum(nums) / a
count = sum(1 for x in nums if x > avg)

print(f"Максимальное: {max_num}")
print(f"Минимальное: {min_num}")
print(f"Среднее: {avg}")
print(f"Чисел больше среднего: {count}")
