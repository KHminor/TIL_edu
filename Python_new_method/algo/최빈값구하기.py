def solution(array):
    dic = dict()
    for i in array:
        if dic.get(i): dic[i] += 1
        else: dic[i] = 1
    mx = max(dic.values())
    return -1 if list(dic.values()).count(mx) != 1 else list(dic.keys())[list(dic.values()).index(mx)]

print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1,1,2,2]))
print(solution([1]))
print(solution([3,3,1]))