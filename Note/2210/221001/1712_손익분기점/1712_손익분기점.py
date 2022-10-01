f,v,c = map(int,input().split())
r = 0
if c > v:
    r = f//(c-v)+1
else:
    r = -1
print(r)
