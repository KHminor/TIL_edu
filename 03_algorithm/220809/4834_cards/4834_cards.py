# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
# 가장 많은 카드의 숫자와 해당 카드가 몇 장인지 출력하는 프로그램을 만드시오.
# 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
# 다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 )

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.

# 출력 예시
#1 9 2
#2 8 1
#3 7 3

import sys
sys.stdin = open('sample_input.txt')

T = int(input())  # 테스트 케이스의 개수

for ct in range(T):
    N = int(input())  # 각 테스트 케이스 별 주어지는 카드의 개수

    ai = input()  # 주어지는 카드를 ai에 담기

    cnt_ai = [0]*10 # 주어지는 카드의 개수를 카운트 하기 위한 리스트 형태의 cnt_ai

    max = max_idx = 0  # 가장 많은 카드 개수 max, 가장 많은 개수의 카드를 가진 카드 번호 max_idx


    # 아래의 코드는 카드의 개수만큼 반복하여 카드 번호인 i를
    # 문자열에서 정수로 변경 후 cnt_ai의 인덱스 값으로 넣어준 후 해당 카운트를 1 증가 시키기
    for i in ai:
        cnt_ai[int(i)] += 1

        # 정수화한 i의 값을 cnt_ai의 인덱스 값으로 지정후 해당 값이 max보다 크다면 max와 max_idx 값을 변경
        if cnt_ai[int(i)] > max:
            max = cnt_ai[int(i)]
            max_idx = int(i)
        # 만약 cnt_ai의 인덱스 int(i)의 값과 max의 값이 같고 int(i)의 값이 max_idx보다 크다면 max_idx값을 변경
        elif cnt_ai[int(i)] == max:
            if int(i) > max_idx:
                max_idx = int(i)

    print(f'#{ct+1} {max_idx} {max}')


