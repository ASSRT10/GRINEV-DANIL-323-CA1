def fibonacci_gen(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1
class SequenceAnalyzer:
    def get_even_numbers(self, generator):
        return [x for x in generator if x % 2 == 0]
analyzer = SequenceAnalyzer()
fib_gen = fibonacci_gen(10)
even_numbers = analyzer.get_even_numbers(fib_gen)
print("Четные числа Фибоначчи (первые 10):")
print(even_numbers)