from collections import deque

# bfs와 delta 를 사용해서 풀기

# 나는 1,1 라고 하지만 배열상 (0,0)
# 상대방은 해당 배열의 가장 마지막인 (n-1, m-1)
def solution(maps):
    que, mx_X_ln, mx_Y_ln = deque([[0, 0, 1]]), len(maps[0])-1, len(maps)-1 # y,x,cnt  
    visit = [[0]*(mx_X_ln+1) for _ in range(mx_Y_ln+1)]

    while que:
        y, x, cnt = que.popleft()
        if visit[y][x]: continue 
        visit[y][x] = 1
        if x == mx_X_ln and y == mx_Y_ln: 
            return cnt
        
        for search in [[-1,0], [0,1], [1, 0], [0,-1]]: # delta 탐색 (위, 오른쪽, 아래, 왼쪽)
            # 현재 좌표에서 델타 방향만큼 더 했을 때 maps 범위내에 있는지, 이동 좌표가 1인지, 방문하지 않았는지 체크
            ny, nx = y+search[0], x+search[1] 
            if 0 <= nx <= mx_X_ln and 0 <= ny <= mx_Y_ln and maps[ny][nx] and not visit[ny][nx]:
                que.append([ny, nx, cnt+1])
            
    return -1 

print(solution([[1,0,1,1,1],[1,0,1,0,1],[0,0,0,0,1]]))



from collections import deque

def solution(maps):
    que, mx_X_ln, mx_Y_ln, result = deque([[0, 0, 1]]), len(maps[0])-1, len(maps)-1, []
    visit = [[0]*(mx_X_ln+1) for _ in range(mx_Y_ln+1)]

    while que:
        x, y, cnt = que.popleft()
        if visit[x][y]: continue 
        visit[x][y] = 1
        if x == mx_X_ln and y == mx_Y_ln: 
            result.append(cnt)
            continue
        
        for search in [[-1,0], [0,1], [1, 0], [0,-1]]: 
            nx, ny = x+search[0], y+search[1] 
            if 0 <= nx <= mx_X_ln and 0 <= ny <= mx_Y_ln and maps[nx][ny] and not visit[nx][ny]:
                que.append([nx, ny, cnt+1])
    
    return min(result) if result else -1


from collections import deque

def solution(maps):
    que, mx_X_ln, mx_Y_ln = deque([[0, 0, 1]]), len(maps[0])-1, len(maps)-1
    visit = [[0]*(mx_X_ln+1) for _ in range(mx_Y_ln+1)]
    while que:
        y, x, cnt = que.popleft()
        if visit[y][x]: continue 
        visit[y][x] = 1
        if x == mx_X_ln and y == mx_Y_ln: return cnt
        for search in [[-1,0], [0,1], [1, 0], [0,-1]]:
            ny, nx = y+search[0], x+search[1] 
            if 0 <= nx <= mx_X_ln and 0 <= ny <= mx_Y_ln and maps[ny][nx] and not visit[ny][nx]: que.append([ny, nx, cnt+1])            
    return -1 