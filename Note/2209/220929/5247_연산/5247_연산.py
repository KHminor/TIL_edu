# bfs를 사용하는 문제?
# 최소 몇 번의 연산
# 연산의 중간 결과도 항상 백만 이하의 자연수 --> 0 또는 음수가 나오면 안됨.
import sys
from collections import deque
sys.stdin = open('sample_input (2).txt')

def min_oper():
    global m, result
    while q:
        n,cnt = q.popleft()
        if n == m:
            result = cnt
            break
        else:
            if cnt > result:
                continue
            else:
                for i in [1,-1,2,-10]:
                    if i == 2:
                        if n*i <= 0: continue
                        if n*i in ch_li: continue
                        else:
                            q.append([n*i, cnt+1])
                            ch_li.append(n*i)
                    else:
                        if n+i <= 0: continue
                        if n+i in ch_li: continue
                        else:
                            q.append([n+i, cnt+1])
                            ch_li.append(n+i)

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    cnt = 0
    result = 1000000
    q = deque()
    q.append([n,cnt])
    ch_li = []
    min_oper()
    print(f'#{tc} {result}')
