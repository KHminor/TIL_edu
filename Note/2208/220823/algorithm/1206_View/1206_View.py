import sys
sys.stdin = open('input (1).txt')
T = 10
for tc in range(1, T+1):
    # 건물의 개수
    N = int(input())
    # 각 건물의 높이에 대한 리스트
    li = list(map(int,input().split()))
    # 결과 값 초기화
    result = 0
    # 가장 앞,뒤의 건물 2개씩은 0의 값이기에 제외 후 조사
    for i in range(2, N-2):
        # 반복 할 때마다 본 건물을 제외한 다른 건물들 중 가장 큰 값 조사 하기 위한 max 초기화
        max = 0
        # 현재 건물의 값을 c_tower 에 저장
        c_tower = li[i]
        # 현재 건물이 좌우 2개의 거리에 있는 건물 중 가장 높을 경우
        if c_tower > li[i-2] and c_tower > li[i-1] and c_tower > li[i+1] and c_tower > li[i+2]:
            # 아래의 for문을 위한 변수로 현재 건물의 위치의 값의 경우 continue
            # 다른 건물의 경우 조사 후 가장 큰 값을 max에 저장 후 계속해서 다음 건물 조사
            ch_num = -2
            for _ in range(5):
                if ch_num == 0:
                    ch_num += 1
                    continue
                else:
                    if li[i+ch_num] > max:
                        max = li[i+ch_num]
                    ch_num += 1
            # 현재 건물에서 주위 건물 중 가장 큰 값과 빼서 result 에 저장
            result += c_tower - max
    print(f'#{tc} {result}')