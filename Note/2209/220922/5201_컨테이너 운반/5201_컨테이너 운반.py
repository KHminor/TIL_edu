# A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행한다고 한다
# 이때 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면,
# 옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램을 만드시오
# 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.
import sys
sys.stdin = open('sample_input (5).txt')
T = int(input())
for tc in range(1,T+1):
# # N: 컨테이너 수, M: 트럭 수
    N,M = map(int,input().split())
    # N 개의 컨테이너의 무게
    w_li = list(map(int,input().split()))
    # M 개의 트럭의 적재가능 용량
    t_li = list(map(int,input().split()))

    w_li.sort(reverse=True)
    t_li.sort(reverse=True)
    s = 0
    for i in t_li:
        for j in range(len(w_li)):
            if i >= w_li[j]:
                s += w_li[j]
                w_li.pop(j)
                break
    print(f'#{tc} {s}')