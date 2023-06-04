a = [1,2,3,4]
b = [5,6,7,8]

result = [x*y for x,y in zip(a,b)]
print(sum(result))