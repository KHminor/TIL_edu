import math
# 최소 공배수
print(math.lcm(2,6,8,14))

#최대 공약수
print(math.gcd(2,6,8,14))


def solution(arr):
    result = 0
    for i in arr:
        if result == 0: result = i
        else:
            result = math.lcm(result, i)
    return result

print(solution([2,6,8,14]))