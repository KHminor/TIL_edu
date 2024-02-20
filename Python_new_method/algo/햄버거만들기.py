def solution(ingredient):
    result = 0
    check = []
    for i in ingredient:
        check.append(i)
        if check[-4:] == [1,2,3,1]:
            result += 1
            del check[-4:]
    return result 


print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))