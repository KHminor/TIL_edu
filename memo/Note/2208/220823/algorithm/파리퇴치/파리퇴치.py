import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    # N = 전체 2차원 배열 크기, M = 파리채 크기
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 잡을 수 있는 최대 값
    max = 0
    # 행으로 봤을 때 파리채로 내리칠 수 있는 횟수
    for i in range(N-M+1):
        # 열로 봤을 때 파리채로 내리칠 수 있는 횟수
        for j in range(N-M+1):
            # 안의 2중 for 문을 돌면 파리채 크기만큼의 좌표값을 다 돌았기에 
            # sum 값을 초기화 해주기.
            sum = 0 
            # 파리채 행의 크기
            for x in range(M):
                # 파리채 열의 크기
                for y in range(M):
                    # 인덱스 값을 이용하여 파리채 좌표값 접근하기
                    sum += arr[i+x][j+y]
                # 현재 파리채 크기만큼의 인덱스 값에 접근 했을 때 모두 더한 값과 max 값 비교
            if sum > max:
                max = sum
    print(f'#{tc} {max}')