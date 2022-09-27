# 정류장에는 교체용 충전지가 있는 교환기가 있고,
# 충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.
# 목적지에 도착하는데 필요한 최소한의 교환횟수를 출력!
# 단, 출발지에서의 배터리 장착은 교환횟수에서 제외한다.

import sys
sys.stdin = open('sample_input (3).txt')
def m_bus(s,num_sum,cnt):
    global n,result
    if cnt >= result:
        return
    else:
        if num_sum >= n:
            result = cnt
            return
        else:
            ln = li[s]
            for i in range(ln,0,-1):
                m_bus(s+i,num_sum+i,cnt+1)
    return
T = int(input())
for tc in range(1,T+1):
    li = list(map(int,input().split()))
    n = li[0]-1
    li = li[1:]
    li.append(0)
    result = n
    m_bus(0,0,-1)
    print(f'#{tc} {result}')