# from collections import deque
# n = int(input())
# li = [0]*(n+1)
# q = deque([[n,0]])

# while True:
#     num,cnt = q.popleft()
#     if num == 1: 
#         print(cnt)
#         break
#     if not num%3 and not li[num//3]:
#         li[num//3] = cnt+1 
#         q.append([num//3,cnt+1])
#     if not num%2 and not li[num//2]: 
#         li[num//2] = cnt+1
#         q.append([num//2,cnt+1])
#     if not li[num-1]:
#         li[num-1] = cnt+1 
#         q.append([num-1,cnt+1])

n = int(input())
li = [1000001]*(n+1) + [1000001]*2
li[1],li[2],li[3] = 0,1,1

for i in range(4, n+1):
    if not i%3 and not i%2: li[i] = min(li[i//3],li[i//2],li[i-1])+1
    elif not i%3: li[i] = min(li[i//3],li[i-1])+1
    elif not i%2: li[i] = min(li[i//2],li[i-1])+1
    else: li[i] = li[i-1]+1
print(li[n])