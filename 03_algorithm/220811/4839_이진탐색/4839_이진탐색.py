# 왼쪽 ==> l = 1
# 오른쪽 ==> r = 400   # 책이 400 페이지일 경우
# 중간 페이지 ==> p //2
# 책의 전체 쪽수오 ㅏ두 사람이찾을 쪽 번호가 주어졌을 떄, 이진 탐색 게임에서 이긴 사람
# 비기면 0 을 출력
import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1,T+1):
    # P = 총 페이지수, Pa = a가 찾을 페이지, Pb = b가 찾을 페이지
    P, Pa, Pb = map(int, input().split())

    # 중앙 값 center와 a, b 가 이진 탐색을 하는 횟수를 따로 받게 변수 초기화
    center = a_cnt = b_cnt = 0
    # left = 1, right = P 로 가장 왼쪽은 1페이지로 가장 오른쪽은 페이지 전체 수로 초기화
    l, r = 1, P

    while True: # a 가 찾는 이진탐색
        a_cnt += 1
        center = (l+r)//2
        if center == Pa:
            break
        elif Pa > center:
            l = center
        elif Pa < center:
            r = center


    l , r, center = 1, P, 0  # a 가 사용한 후 초기화

    while True: # b 가 찾는 이진탐색
        b_cnt += 1
        center = (l + r) // 2
        if center == Pb:
            break
        elif Pb > center:
            l = center
        elif Pb < center:
            r = center


    if a_cnt < b_cnt: # B 가 이진 탐색을 더 많이 실행 했기에 A의 승
        print(f'#{tc} A')
    elif a_cnt > b_cnt: # A 가 이진 탐색을 더 많이 실행 했기에 B의 승
        print(f'#{tc} B')
    else: # 비겼을 경우 0을 출력력
       print(f'#{tc} 0')

