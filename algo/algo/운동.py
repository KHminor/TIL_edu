import sys
input = sys.stdin.readline

N,m,M,T,R = map(int,input().split())
be_m = m
cnt = 0

if M-m >= T: # 추가 혈압이 초과 되지 않는 범위
    for _ in range(N):
        if m+T <= M: # 맥박 초과 X
            m += T
            cnt += 1
        else:
            while (m+T > M):
                cnt += 1
                if m-R >= be_m: m -= R
                else: 
                    m = be_m
                    break
            m += T
            cnt += 1
    print(cnt)
else: print(-1)