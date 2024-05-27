def solution(quiz):
    result = []
    for i in quiz:
        li = i.replace("=","").split()
        if li[1] == "+" and int(li[0])+int(li[2]) == int(li[-1]): result.append("O")
        elif li[1] == "-" and int(li[0])-int(li[2]) == int(li[-1]): result.append("O")
        else: result.append("X")
            
    return result

def solution(quiz): return ["O" if eval(i.replace("=","==")) else "X" for i in quiz]


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
# print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))