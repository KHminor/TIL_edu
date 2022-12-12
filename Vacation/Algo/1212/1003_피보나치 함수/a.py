a = [1,2]
b = [2,3]

print(a+b)

c = a+b
jjac = hol = 0
for i in range(len(c)):
    if i %2:
        hol += c[i]
    else:
        jjac += c[i]
print(jjac, hol)