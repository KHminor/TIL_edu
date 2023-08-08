for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = 11*n*n
    # dfs 사용
    stack = [[0, 0, arr[0][0]]]
    while stack:
        x,y,hab = stack.pop()
        if x == n-1 and y == n-1: 
            if result > hab: 
                result = hab
            continue
        elif hab >= result: continue
        # 오른쪽, 아래만 탐색
        for i,j in [[0, 1], [1, 0]]:
            dx, dy = x+i, y+j
            if 0<=dx<n and 0<=dy<n:
                stack.append([dx, dy, hab+arr[dx][dy]])
    print('#%d'%tc, end=' ')
    print(result)