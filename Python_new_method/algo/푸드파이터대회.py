def solution(food):
    li = []
    for i in range(1,len(food)):
        if food[i]//2:
            li.append(str(i)*(food[i]//2))
    s = "".join(li)
    return s+"0"+s[::-1]

print(solution([1,3,4,6]))
print(solution([1,7,1,2]))