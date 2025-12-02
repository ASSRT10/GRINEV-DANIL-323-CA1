a = input("Введите текст: ")
b = set(c.lower() for c in a.split())
print(f"Уникальные слова: {len(b)}")
длинные_слова = {c for c in b if len(c) > 5}
print(f"Длинные слова: {длинные_слова}")
ключевые_слова = any(c in b for c in ["python", "programming"])
print(f"Найдены ключевые слова: {ключевые_слова}")