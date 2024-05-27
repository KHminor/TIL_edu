n = int(input())
cnt = 0
hap = 0

for i in range(1, n+1):
    cnt += 1
    hap += i
    if hap > n: break
print(cnt-1) 

n = int(input())
cnt = 0
hap = 0

for i in range(1, n+1):
    cnt += 1
    hap += i
    if hap > n:
        cnt -= 1 
        break
print(cnt) 

# n=int(input())
# sum=0
# result=0
# for i in range(1, n+1):
#     sum+=i
#     result+=1
#     if sum>n:
#         result-=1
#         break
    
# print(result)