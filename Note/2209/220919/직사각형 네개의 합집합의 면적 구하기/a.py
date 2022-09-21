from pprint import pprint

visited = [[0]*101 for _ in range(101)]     # 방문 체크

cnt = 0                                     # 카운트 변수 초기화
for _ in range(4):                          # 입력은 4줄
    si,sj,ei,ej = map(int,input().split())  # 입력값 받기
    x,y = ei-si, ej-sj                      # 가로,세로 반복횟수 

    for i in range(x):
        for j in range(y):
            if visited[si+i][sj+j] == 1:    # 해당 방문값이 1의 경우 다음
                continue
            else:                           # 1이 아닐 경우 방문 후 cnt 1증가
                visited[si+i][sj+j] = 1
                cnt += 1
print(visited)
print(cnt)