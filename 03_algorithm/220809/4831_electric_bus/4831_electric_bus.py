# 한번 충전으로 이동할 수 있는 최대 정류장 수 = K # 3
# 충전기가 설치된 정류장 수 = M   # 5
# 버스의 종점 = N  # 10
# 출발지에는 충전이 항상 되어있어서 처음 시작은 +3,
# 카운팅은 출발지에서 하지 않음
# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력

# K = 이동 정류장 수 ,
# N  = 버스 종점,
# M  = 충전기 설치된 정류장 수
# 몇 번 충전을 해야 종점에 도착할 수 있는지 출력.
import sys
sys.stdin = open('sample_input.txt')

T = int(input()) # 테스트 케이스

for tc in range(1,T+1): # 테스트 케이스만큼 반복
    K, N, M = map(int,input().split())
    charge = list(map(int,input().split()))
    charge_cnt_li = [0]*(N+1)

    for charge_num in charge:
        charge_cnt_li[charge_num] += 1  # 주유소 위치

    start = charge_cnt = 0  # 시작점과 차징 횟수 초기화
    boo = True
    while boo:
        for i in range(K,0,-1):
            now_start = start
            if charge_cnt_li[start + i] == 1:
                start += i
                charge_cnt += 1
                if start + K > N:
                   boo = False
                   break
                else:
                    break
            # 현재 start 주유한곳에서 이동 가능한 거리까지 움직인 경우
            # 도착한 곳이 종점이라면 아래코드
            elif start + K == N:
                boo = False
                break

            for j in range(1,K+1):
                if charge_cnt_li[start + j] == 1:
                    break
                else:
                    if j == K:
                        charge_cnt = 0
                        boo = False
                        break

    print(f'#{tc} {charge_cnt}')


