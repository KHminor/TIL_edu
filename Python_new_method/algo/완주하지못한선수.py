def solution(participant, completion):
    dic = {i:0 for i in set(participant)}
    for i in participant: dic[i] += 1
    for i in completion: dic[i] -= 1
    for i in dic.keys():
        if dic[i] != 0: return i

# # print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
# # print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))

