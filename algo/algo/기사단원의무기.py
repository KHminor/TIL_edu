def solution(number, limit, power):
    result = [0]*number
    result[0] = 1
    s = set()
    for i in range(2,number+1):
        for j in range(1,int(i**(1/2))+1):
            if not i%j:
                s.add(j)
                s.add(i//j)
        result[i-1] = power if len(s) > limit else len(s)
        s.clear()
    return result

print(solution(5,3,2))
print("=============")
print(solution(10,3,2))