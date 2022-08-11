import sys
sys.stdin = open('sample_input.txt')
T = int(input())

# li = 좌측 상단 i
# lj = 좌측 상단 j
# ri = 우측 하단 i
# rj = 우측 하단 j
# color 1 = 빨강, 2 = 파랑 , 3 = 보라

for ct in range(1,T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    for _ in range(N):
        li, lj, ri, rj, color = map(int,input().split())  # li:2, lj:2, ri:4, rj:4, color:1(빨강)
        for i in range(ri-li+1): # 우측 하단 - 좌측 상단 + 1 을 하여 가로로 채울 박스의 길이 체크
            for j in range(rj-lj+1): # 위와 마찬가지로 세로로 채울 박스의 길이 체크
                arr[li+i][lj+j] += color


        cnt = 0  # 해당 지역이 겹쳤는지 확인하기 위한 cnt 초기화
        for x in range(10):
            for y in range(10):
                if arr[x][y] >= 3: # 10*10 형태의 공간에서 해당 지역이 3보다 크면 겹쳐 있는 구역이기에 cnt체크
                    cnt += 1

    print(f'#{ct} {cnt}')