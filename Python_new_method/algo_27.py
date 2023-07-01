def solution(s): 
    print(sorted(list(s)))
    return ''.join(sorted(s, reverse=True))


print(solution("Zbcdefg"))
