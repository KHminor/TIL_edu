def f(n): # 팩토리얼
    if n <= 1:
        return 1
    else:
        return n * f(n-1)

print(f(5))