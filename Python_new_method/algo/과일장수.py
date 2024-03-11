def solution(k, m, score):
    result,cnt = 0,0
    for i in sorted(score,reverse=True):
        cnt += 1
        if cnt == m: 
            result += i*m
            cnt = 0
    return result



print(solution(3,4,[1, 2, 3, 1, 2, 3, 1]))
print(solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))