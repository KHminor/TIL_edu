def solution(s): 
    ln = len(s)
    return s[ln//2] if ln%2 else s[ln//2-1:ln//2+1]


def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]

print(string_middle("qwer"))

print(solution("qwer"))