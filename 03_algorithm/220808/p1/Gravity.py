import sys
sys.stdin = open('input.txt')

tc = int(input()) # 테스트 케이스 수

for t in range(tc): 
    weith = int(input())  # 상자를 담는 가로 길이
    # 아래는 각각의 상자 길이를 li라는 list 공간에 저장
    li = list(map(int,input().split()))

    result = 0  # 낙차의 크기가 가장 큰 결과값

    # 모든 상황에 대한 낙찻값을 위해 전체 순회
    for i in range(weith):
        # 아래의 코드는 우측으로 90도 돌렸을 경우
        # 기존의 가로 길이가 세로 길이가 되어 낙차하는 방향이 되는데
        # 우선 기준 블록으로부터 밑에 아무런 블럭이 없다 생각을 하고
        # 해당 블록이 떨어질 수 있는 최대 길이를 max_h에 저장한다.
        # 여기서 i+1을 하는 이유는 기존의 블럭 위치에서 떨어질 때는
        # 한칸을 더 내려간 이후 시점부터 낙하를 하기 때문이다.
        max_h = weith - (i+1)

        # 아래는 해당 블록 다음으로 오는 상자들 중에
        # 해당 블록보다 크거나 같은 블록을 찾는 반복문
        for j in range(i+1, weith):
            # 기준 블록보다 j 번째 블록이 크거나 같은 값의 경우
            # 낙하 할 수 있는 칸의 개수가 줄어들기에 하나씩 차감
            if li[j] >= li[i]:
                max_h -= 1

        # 아래의 코드는 방금 구한 낙차 값인 max_h 가
        # 기존의 낙차의 크기가 가장 큰 결과값인 result 보다
        # 크다면 max_h 값을 result에 넣어주는 코드
        if max_h > result:
            result = max_h

    print(f'#{tc}번째의 결과는 {result}')
