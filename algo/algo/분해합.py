n = int(input())
result = 0
for i in range(n-1,0,-1):
    if n == i+sum(list(map(int,str(i)))): result = i
if result: print(result)
else: print(0)