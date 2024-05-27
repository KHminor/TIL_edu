def solution(X, Y):
    li = [0]*10
    result = []
    for i in X: li[int(i)] += 1
    for i in Y: 
        if li[int(i)] > 0: 
            li[int(i)] -= 1
            result.append(i)
    return "-1" if result == [] else str(int("".join(sorted(result,reverse=True))))

# def solution(x,y):
#     result = []
#     d_x,d_y = {str(i):0 for i in range(10)},{str(i):0 for i in range(10)}
#     for i in x: d_x[i] += 1
#     for i in y: d_y[i] += 1
#     li = [min(d_x[str(i)],d_y[str(i)]) for i in range(10)]
#     state = True
#     for i in range(9,-1,-1):
#         if li[i] != 0:
#             if state: state = False 
#             if i == 0: result.append("0")
#             else: result.append(str(i)*li[i])
#     return "-1" if state else "".join(result)


def solution(x,y):
    xy = set(x) & set(y)
    if not xy: return "-1"
    elif len(xy) == 1 and "0" in xy: return "0"
    return "".join(sorted([i*min(x.count(i),y.count(i)) for i in xy], reverse=True))

print(solution("100","2345"))
print(solution("100","203045"))
print(solution("100","123450"))
print(solution("12321","42531"))
print(solution("5525","1255"))
# print(solution("0155","5510"))