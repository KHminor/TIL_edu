# 가로 길이는 항상 1000 이하
# 맨 왼쪽 , 맨 오른쪽 2칸씩은 건물이 지어지지 않는다
# 각 빌딩의 높이는 최대 255.
# 조망권 확보 : 좌우 양쪽의 거리가 2이상의 공간이 확보 될 경우
# 구할 것 : 조망권이 확보된 세대의 수
import sys
sys.stdin = open('input.txt')

tc = 1
while tc <= 10:
    t_weith = int(input()) # 테스트 가로 길이
    b_list = list(map(int,input().split()))  # 각각의 빌딩의 높이를 담고 있는 리스트
    cnt = 0  # 조망권 확보된 세대의 수
    for i in range(2,len(b_list)-2):   # 좌우 2칸씩에는 건물이 없기에 제외하고 반복문
        # 아래의 코드는 기준 건물에서 좌우 2씩의 거리에 있는 건물보다 기준 건물이 큰지 확인하는 코드
        if b_list[i] > b_list[i-1] and b_list[i] > b_list[i+1] :
            if b_list[i] > b_list[i-2] and b_list[i] > b_list[i+2]:

                # 기준 건물을 제외하고 좌우 2거리에 있는 건물중 가장 큰 건물을 확인하기 위해
                # 우선 기준 건물에서 -2거리에 있는 건물을 기준잡기
                max_height = b_list[i-2]

                for j in range(-1,3):
                    if b_list[i+j] == b_list[i]:
                        continue
                    elif b_list[i+j] > max_height:
                        max_height = b_list[i+j]

                # 기준 건물을 기반으로 좌우 2거리에 있는 건물중 가장 높은 건물과의
                # 차이만큼 cnt 에 추가해주기.
                cnt += b_list[i] - max_height
    print(f'#{tc} {cnt}')
    tc += 1
