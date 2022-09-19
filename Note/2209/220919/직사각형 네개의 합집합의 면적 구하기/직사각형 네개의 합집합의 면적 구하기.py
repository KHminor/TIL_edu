from pprint import pprint
visited = [[0]*10 for _ in range(10)]

cnt = 0
for _ in range(4):
    si,sj,ei,ej = map(int,input().split())
    x,y = ei-si, ej-sj

    for i in range(x):
        for j in range(y):
            if visited[si+i][sj+j] == 1:
                continue
            else:
                visited[si+i][sj+j] = 1
                cnt += 1

pprint(visited)
print(cnt)
