# 유클리드 호제법으로 푼 최대공약수, 최소공배수

def gcd(n,m):
    while m != False:
        n,m = m, n%m    
    return n

def lcm(n,m,x):
    return n*m//x

def solution(n, m):
    x = gcd(n,m) 
    return [x,lcm(n,m,x)]


# -------------------------------------

def solution(n, m):
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]


print(solution(3, 12))
