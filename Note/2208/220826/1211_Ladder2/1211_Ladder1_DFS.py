T = 10
for _ in range(T):
    tc = int(input())
    # 배열 범위
    N = 100
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 큐 초기화
    s = []
    # 출발 좌표 찾기 (0,?) 에서 시작하기에 하나의 for문 만 이용하여 조사
    for i in range(N):
        if arr[0][i] == 1:
            s.append([0,i])

    # 가장 짧은 열과 그 열에서 목적지 까지의 거리를 담을 변수 초기화
    move_li = []
    short_d = []

    # s 에 값이 있을 때까지
    while s:
        # 시작 좌표를 담은 q의 가장 처음 값을 si,sj에 할당
        si,sj = s.pop()
        # 방문체크
        visited = [[0] * N for _ in range(N)]
        # 이동전 시작 위치를 기억하기 위한 변수
        num = sj
        # 이동 거리 변수 초기화
        move = 0
        # 시작 좌표로 부터 이동 가능한 경로를 담을 q2 초기화
        s2 = []
        while True:
            # 현재 move_li 에 값이 있으며 해당 값이 현재 move보다 크거나 같을 경우 계속해서 조사 X
            if move_li and move_li[0] <= move:
                break
            # 현재 좌표를 방문 표시
            visited[si][sj] = 1
            # 만약 도착지점에 방문했을 경우
            if visited[99][sj] == 1:
                # 만약 처음 조사하는 경우라면
                if not move_li:
                    # 현재 이동 횟수와, 가장 처음에 출발한 열의 값을 short_d에 추가 후 반복문 탈출
                    move_li.append(move)
                    short_d.append(num)
                    break
                # 처음 조사하는 것이 아닐 경우 move_li의 처음값과 비교 후 현재 move의 값이 더 작은 경우 추가
                else:
                    if move_li[0] > move:
                        move_li[0] = move
                        short_d[0] = num
                    break
            # 좌,우,하
            for i,j in [[0, -1], [0, 1], [1, 0]]:
                if 0 <= si + i < N and 0 <= sj + j < N and arr[si+i][sj+j] == 1 and not visited[si+i][sj+j]:
                    s2.append([si+i,sj+j, move+1])
                    break
            # s2에 값이 존재할 경우 si,sj,move 값 할당.
            if s2:
                si,sj,move = s2.pop()

    print(f'#{tc}', end=' ')
    print(*short_d)