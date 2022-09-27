# 그냥 좌표의 숫자를 모두 곱하고 난뒤
# 곱한 값 m /= (100)**(n-1)
# print(100**2)

def digital(i,m):
    global result
    if i == n:
        if m > result:
            result = m
            return
        else:
            return
    else:
        # if result >= m:
        #     return
        # else:
        for j in range(n):
            if not visited[j] and arr[i][j] != 0:
                visited[j] = 1
                m *= arr[i][j]
                digital(i+1,m)
                visited[j] = 0
                m //= arr[i][j]
# T = int(input())
# for tc in range(1,T+1):
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visited = [0]*n
    m = 1
    result = 0
    digital(0,m)
    result = round(result/100**(n-1),6)
    result = format(result, '.6f')
    print(f'#{tc} {result}')

