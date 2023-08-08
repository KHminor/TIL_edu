# def search(hap, cnt):
#     global mx_hap
#     if cnt == n-1:
#         mx_hap = min(mx_hap, hap)
#         return
#     elif hap >= mx_hap: return
#     for i in range(n):
#         if arr[cnt+1][i] and not visited[i]: # 해당 값이 0이 아니고, 방문하지 않았다면
#             visited[i] = 1
#             search(hap+arr[cnt+1][i], cnt+1)
#             visited[i] = 0
#     return

# for tc in range(1, int(input())+1):
#     n = int(input())
#     arr = [list(map(int,input().split())) for _ in range(n)]
#     visited = [0]*n
#     mx_hap = 101*n
#     for s in range(1, n):
#         visited[s] = 1
#         search(arr[0][s], 0)
#         visited[s] = 0
#     print('#%d'%tc, end=' ')
#     print(mx_hap)


def search(s, hap, cnt):
    global mx_hap
    if cnt == n-2:
        mx_hap = min(mx_hap, hap+arr[s][0])
        return
    if hap >= mx_hap: return
    for i in range(1,n):
        if arr[s][i] and not visited[i]: # 해당 값이 0이 아니고, 방문하지 않았다면
            visited[i] = 1
            search(i, hap+arr[s][i], cnt+1)
            visited[i] = 0
    return

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visited = [0]*n
    mx_hap = 101*n

    for s in range(1, n):
        visited[s] = 1
        search(s, arr[0][s], 0)
        visited[s] = 0
    print('#%d'%tc, end=' ')
    print(mx_hap)