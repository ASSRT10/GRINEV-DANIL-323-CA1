import string
text = input("Введите текст: ")
words = [word.strip(string.punctuation).lower() for word in text.split()]
longest = max(words, key=len)
shortest = min(words, key=len)
avg_len = sum(len(word) for word in words) / len(words)
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:5]
print(f"Самое длинное слово: {longest}")
print(f"Самое короткое слово: {shortest}")
print(f"Средняя длина: {avg_len:.1f}")
print(f"Топ-5 слов: {top_words}")