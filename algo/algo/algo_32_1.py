# def solution(n, m):
#     gcd = lambda a, b : b if not a%b else gcd(b,a%b) 
#     lcm = lambda a, b : a*b//gcd(a,b)
#     return [gcd(n,m), lcm(n,m)]

def gcd(n,m):
    while m != False:
        n,m = m, n%m
    return n

def lcm(n,m):
    return n*m//gcd(n,m)

def solution(n,m):
    return [gcd(n,m), lcm(n,m)]


print(solution(3,12))
