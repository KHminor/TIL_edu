def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x-1)


N = 5
print(factorial(N))
