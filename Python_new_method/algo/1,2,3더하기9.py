# def find(num,cnt):
#     global result
#     if cnt == 0 or num == 0:
#         if num == 0: result = (result+1)%1000000009
#         return
#     for i in range(1,4):
#         if 0 > num-i or 0 > cnt-1: break 
#         find(num-i,cnt-1)

# import sys
# input = sys.stdin.readline
# for _ in range(int(input())):
#     result = 0
#     n,m = map(int,input().split())
#     find(n,m)
#     print(result)

# dp 활용해보기

def startSetting():
    li[1][1] = 1
    
    li[2][1] = 1
    li[2][2] = 1
    
    li[3][1] = 1
    li[3][2] = 2
    li[3][3] = 1


import sys
input = sys.stdin.readline
val = 1000000009
li = [[0]*1001 for _ in range(1001)]
startSetting()
for i in range(4,1001):
    for j in range(1,i+1): li[i][j] = (li[i-1][j-1]+li[i-2][j-1]+li[i-3][j-1])%val

for _ in range(int(input())):
    n,m = map(int,input().split())
    print(sum(li[n][:m+1])%val)