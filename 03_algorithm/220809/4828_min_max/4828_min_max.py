# 주소 :https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

# [입력]
#
# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
#
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
#
# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
#
# [출력]
#
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

import sys
sys.stdin = open('sample_input.txt')

T = int(input()) # 테스트 케이스의 수

for cnt in range(T):  # 테스트 케이스의 수만큼 반복
    N = int(input()) # 각 테스트 케이스의 양의 정수 개수

    ai = list(map(int,input().split()))  # N 개의 양의 정수를 공백을 기준으로 list로 담기

    max = min = ai[0]

    for i in range(1,N):
        # 리스트 타입인 ai 의 0번째 인덱스 값인 max와 ai[i]를 비교 후 ai[i] 의 값이 크다면 max값을 ai[i]로 변경
        if ai[i] > max:
            max = ai[i]
        # 리스트 타입인 ai 의 0번째 인덱스 값인 min와 ai[i]를 비교 후 ai[i] 의 값이 작다면 min값을 ai[i]로 변경
        elif ai[i] < min:
            min = ai[i]

    print(f'#{cnt+1} {max - min}')
