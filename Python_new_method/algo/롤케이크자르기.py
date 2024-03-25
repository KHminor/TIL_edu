from collections import Counter
def solution(topping):
    result = 0
    bro = Counter(topping)
    chul = set()
    for i in topping:
        bro[i] -= 1
        if not bro[i]: del bro[i]
        chul.add(i)
        if len(bro) == len(chul): result += 1
    return result

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1,2,3,1,4]))
print({1,2,3}=={3,2,1})


def solution(topping):
    result = 0
    for i in range(1,len(topping)):
        if set(topping[:i]) == set(topping[i:]): result += 1
    return result