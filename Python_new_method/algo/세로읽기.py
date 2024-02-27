def solution(my_string, m, c):
    li = [my_string[i*m:(i+1)*m] for i in range(len(my_string)//m)]
    return "".join([i[c-1] for i in li])

def solution(my_string, m, c):
    return my_string[c-1::m]

print(solution("ihrhbakrfpndopljhygc",4,2))