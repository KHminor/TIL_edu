import sys
input = sys.stdin.readline
n = int(input())
li = sorted(list(map(int,input().rstrip('\n').split())))
x = int(input())
result = 0

for i in range(n):
    s = i+1
    e = n-1
    while e>=s and n-1>=i:
        moc = (s+e)//2
        check = li[i]+li[moc]
        if check == x: 
            result += 1
            break
        elif check > x: e = moc-1
        else: s = moc+1

print(result)


# import sys
# from itertools import combinations
# input = sys.stdin.readline
# n = int(input())
# li = list(map(int,input().rstrip('\n').split()))
# x = int(input())
# result = 0
# for i in list(combinations(li,2)):
#     if sum(i) == x: result += 1
# print(result)


# import sys
# input = sys.stdin.readline
# n = int(input())
# li = sorted(list(map(int,input().rstrip('\n').split())))
# x = int(input())
# result = 0

# for i in range(1,n):
#     for j in range(0,i):
#         if li[i]+li[j] == x:
#             result += 1
#             break
# print(result)