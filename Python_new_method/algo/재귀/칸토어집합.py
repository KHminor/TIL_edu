def cantoer(n):
    if n == 1: return '- -'
    else: return cantoer(n-1) + ' '*(3**(n-1)) + cantoer(n-1)

while True:
    try:
        n = int(input())
        if n == 0: print('-')
        else: print(cantoer(n))
    except EOFError:break