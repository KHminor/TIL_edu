# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     a,b = map(int,input().rstrip('\n').split())
#     c_a,c_b = a,b

#     while c_a != c_b:
#         if c_a > c_b: c_b += b
#         else: c_a += a
#     print(c_a)

# 유클리드 호제법
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a,b = map(int,input().rstrip('\n').split())
    result = a*b
    if b>a: a,b = b,a
    while b != 0:
        a,b = b, a%b
    print(result//a)