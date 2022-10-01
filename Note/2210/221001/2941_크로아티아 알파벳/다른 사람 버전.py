a = input()
b = ["c=","c-","dz=","d-","lj","nj","s=","z="]
result = 0
temp = 0
for x in b:
    if x in a:
        a = a.replace(x,"A")
print(len(a))