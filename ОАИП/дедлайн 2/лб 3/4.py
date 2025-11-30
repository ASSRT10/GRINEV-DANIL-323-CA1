a = {
    "Ноутбук": {"price": 50000, "sold": 15},
    "Мышь": {"price": 1000, "sold": 45},
    "Клавиатура": {"price": 2500, "sold": 30},
    "Монитор": {"price": 30000, "sold": 8}
}
b = max(a, key=lambda x: a[x]["sold"])
c = sum(a[p]["price"] * a[p]["sold"] for p in a)
d = max(a, key=lambda x: a[x]["price"] * a[x]["sold"])
print(f"Самый продаваемый: {b}")
print(f"Общая выручка: {c}")
print(f"Товар с макс выручкой: {d}")
