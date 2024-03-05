def solution(n, lost, reserve):
    dic = {i:1 for i in range(1,n+1)}
    for i in reserve: dic[i] += 1
    s_re,s_lo = set(reserve),set(lost)
    for i in s_re.intersection(s_lo): dic[i] -=1
    for i in s_lo-s_re:
        dic[i] -= 1
        if dic[i] == 0:
            if dic.get(i-1) and dic[i-1] > 1: dic[i-1],dic[i] = dic[i-1]-1,1
            elif dic.get(i+1) and dic[i+1] > 1: dic[i+1],dic[i] = dic[i+1]-1,1
    return sum([1 if i >= 1 else 0 for i in dic.values()])


print(solution(5,[1,2,3,5,4],[1, 3, 5]))
# print(solution(5,[2, 4],[1, 3, 5]))
# print(solution(5,[2, 4],[3]))
# print(solution(3,[3],[1]))