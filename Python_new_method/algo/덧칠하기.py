def solution(n, m, section):
    result = 0
    li = [0]*(n+1)
    for i in section:
        if not li[i]:
            try: 
                li[i:i+m] = [1]*m
                result += 1
            except: result += 1
    return result

print(solution(8,4,[2, 3, 6]))
print(solution(5,4,[1, 3]))
print(solution(4,1,[1, 2, 3, 4]))