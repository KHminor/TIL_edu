# import sys
# input = sys.stdin.readline
for tc in range(int(input())):
    n,m = map(int,input().split())
    li = [float('inf')]
    for _ in range(m):
        li2 = list(map(int,input().split()))
        for i in range(len(li)):
            if li[i] > li2[0]:
                li[i:i] = li2
                break
    li.reverse()
    print('#%d'%(tc+1), end=' ')
    print(*li[1:11])

# for test in range(1,int(input())+1):
#     N, M = map(int, input().split())
#     arr = [float('inf')]
#     for _ in range(M):
#         a = list(map(int, input().split()))
#         for i in range(len(arr)):
#             if a[0] < arr[i]:
#                 arr[i:i] = a
#                 break
#         print(arr)
#     print(f'#{test}',end=' ')
#     print(*arr[-11:-1][::-1])