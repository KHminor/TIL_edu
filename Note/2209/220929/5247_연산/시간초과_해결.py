# bfs를 사용하는 문제?
# 최소 몇 번의 연산
# 연산의 중간 결과도 항상 백만 이하의 자연수 --> 0 또는 음수가 나오면 안됨.
# 코드를 줄이고 가지치기도 했지만 함수를 이용해서 찾을 때 좀 더 느린거 같음...
import sys
from collections import deque
sys.stdin = open('sample_input (2).txt')

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    q = deque([n])
    result = 0
    ch_li = [0] * 1000001
    while q:
        n = q.popleft()
        if n == m:
            result = ch_li[n]
            break
        else:
            for i in [n+1,n-1,n*2,n-10]:
                if 0 < i <= 1000000 and ch_li[i] == 0:
                    ch_li[i] = ch_li[n] + 1
                    q.append(i)
    print(f'#{tc} {result}')
