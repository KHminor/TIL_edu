def solution(a, b, n):
    result = 0
    while n >= a:
        x = n//a*b
        result += x
        n = x+n%a
    return result

print(solution(4,2,20))

20-20+5*210

4+2