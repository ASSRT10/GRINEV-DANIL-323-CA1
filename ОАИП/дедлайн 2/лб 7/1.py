def sum_numbers(*args: int | float) -> int | float:
    return sum(args)
print(sum_numbers(1, 2, 3, 4, 5))