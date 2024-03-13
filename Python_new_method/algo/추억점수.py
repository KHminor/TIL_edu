def solution(name, yearning, photo):
    dic = {name[i]:yearning[i] for i in range(len(name))}
    result = [0]*len(photo)
    for i,p in enumerate(photo):
        for idx,j in enumerate(p):
            if dic.get(j): result[i] += dic[j]
    return result

print(solution(["may", "kein", "kain", "radi"],
            [5, 10, 1, 3],
            [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))