temps = [15, 18, 12, 20, 16, 14, 19, 17, 13, 21, 15, 16, 18, 20]
max_temp = max(temps)
min_temp = min(temps)
avg_temp = sum(temps) / len(temps)
above_avg = len([t for t in temps if t > avg_temp])
sorted_temps = sorted(temps)
fahrenheit = [t * 9/5 + 32 for t in temps]
print(f"Температуры: {temps}")
print(f"Максимальная: {max_temp}°C")
print(f"Минимальная: {min_temp}°C")
print(f"Средняя: {avg_temp:.1f}°C")
print(f"Дней выше средней: {above_avg}")
print(f"Отсортированные: {sorted_temps}")
print(f"Фаренгейты: {[round(f, 1) for f in fahrenheit]}")