def solution(n):
    mtx = [[0]*n for _ in range(n)]
    i,vi,j,vj = 0,n-1,0,n-1
    
    s = 1
    r = 0
    while s <= n*n:
        while j <= vj and mtx[i][j] == 0:
            mtx[i][j] = s
            s += 1
            j += 1
        i,j = i+1,j-1

        while i <= vi and mtx[i][j] == 0:
            mtx[i][j] = s
            s += 1
            i += 1
        i,j = i-1,j-1

        while j >= r and mtx[i][j] == 0:
            mtx[i][j] = s
            s += 1
            j -= 1
        i,j = i-1,j+1

        while j >= r and mtx[i][j] == 0:
            mtx[i][j] = s
            s += 1
            i -= 1
        i,j = i+1,j+1

        vi,vj = vi-1,vj-1
        r += 1
    return mtx



def solution(n):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    y, x = 0, -1

    arr = [[0] * n for _ in range(n)]
    cnt = 1
    direction = 0
    while cnt <= n**2:
        ny, nx = y + dy[direction], x + dx[direction]
        if 0 <= ny < n and 0 <= nx < n and not arr[ny][nx]:
            arr[ny][nx] = cnt
            cnt += 1
            y, x = ny, nx
        else:
            direction = (direction + 1) % 4

    return arr