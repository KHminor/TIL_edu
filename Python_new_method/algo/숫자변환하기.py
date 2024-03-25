from collections import deque
def solution(x, y, n):
    if x == y: return 0
    visit = {x}
    q = deque([[x+n,1],[x*2,1],[x*3,1]])
    while q:
        val,cnt = q.popleft()
        if val == y: return cnt
        for i in [val+n,val*2,val*3]:
            if y >= i and i not in visit:
                visit.add(i) 
                q.append([i,cnt+1])
    return -1

print(solution(10,40,5))
print(solution(10,40,30))
print(solution(2,5,4))
print(solution(1,1,4))