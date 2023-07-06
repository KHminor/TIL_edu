def solution(pgr, spd):
    li, result, check = [(100-pgr[i])//spd[i]+1 if (100-pgr[i])%spd[i] else (100-pgr[i])//spd[i] for i in range(len(spd))], [], 0
    for i in range(len(li)):
        if not result: result, check = [1], li[i]
        else:
            if li[i-1] >= li[i] or check >= li[i]: result[-1] += 1
            else: 
                check = li[i]
                result.append(1)
    return result

# print(solution([93, 30, 55], [1, 30, 5]))
# print(solution([95, 90, 99, 98, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([55, 60, 65], [5, 10, 7]))
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# progresses : [1, 1, 50] / speeds : [100, 2, 1] / answer : [1,2]

