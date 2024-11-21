def factorial(n):
    if n == 0:
        return 1
    out = n * factorial(n - 1)
    print("N = %i, returned value = %i"% (n, out))
    return out
n = 10
print("Factorial of", n, "is:", factorial(n))