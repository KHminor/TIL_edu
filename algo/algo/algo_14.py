import re

def solution(s):
    answer = []
    li = re.findall(r'\{.*?\}', s[1:-1])
    li.sort(key=len)
    li = [set(map(int,i.strip('{}').split(','))) for i in li]
    if len(li) == 1: answer =  list(li[0])
    else:
        for i in range(len(li)-1):
            if i == 0: answer.append(list(li[i])[0])
            answer.append(list(li[i+1].difference(li[i]))[0])
    return answer


# solution("{{123}}")

from collections import Counter

def solution(s):

    # s = re.findall('\d+', s)
    s = Counter(re.findall('\d+', s))
    # s = Counter(re.findall('\d', s))
    print(s)

    return [int(k) for k,v in sorted(s.items(), key=lambda x:x[1], reverse=True)]

print(solution("{{20,111},{111}}"))




# string = "{4,2,3},{3},{2,3,4,1},{2,3}"
# # \{는 { 를 의미하고 마찬가지로 \}는 } 를 의미
# # 그리고 .*? 는 0개 이상의 임의의 문자를 의미하는데 ?를 넣어줌으로서 
# # 해당 패턴이 최소한으로 매칭되도록 하기.
# parsed_list = re.findall(r'\{.*?\}', string) 
# parsed_list.sort(key=len)
# print(parsed_list)
