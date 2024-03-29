# def solution(score):
#     li = [sum(i)/2 for i in score]
#     result = [len(score)]*len(score)
#     for i in range(len(li)):
#         for j in range(len(li)):
#             if i!=j and li[i] >= li[j]: result[i]-=1
#     return result


def solution(score):
    li = [sum(i)/2 for i in score]
    s_li = sorted(li,reverse=True)
    return [s_li.index(i)+1 for i in li ]

print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))
