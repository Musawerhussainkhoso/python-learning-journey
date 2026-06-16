#Find the factorial of a number using recursion.
def factorial(n):
    if n == 1:  # Base case
        return 1

    return n * factorial(n - 1)

print(factorial(5))