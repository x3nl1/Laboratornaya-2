def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = int(input("Введите число для вычисления факториала: "))
result = calculate_factorial(n)
print(result)
