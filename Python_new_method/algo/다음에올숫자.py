def solution1(c):
    a,b,state = 0,0,True
    for i in range(1,3):
        if i == 1:
            a = c[1]-c[0]
            b = c[1]//c[0]
        else:
            if a != c[i]-c[i-1]: state = False
    return c[-1]+a if state else c[-1]*b


def solution(c):
    if c[1]-c[0] == c[2]-c[1]:
        return c[-1]+c[2]-c[1]
    else: return c[-1]*(c[2]//c[1])

print(solution1([0,2,4,8]))
print(solution([0,2,4,8]))
