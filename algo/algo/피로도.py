# from itertools import permutations

# def solution(k, dungeons):
#     result = 0    
#     for i in list(permutations(dungeons,len(dungeons))):
#         pe,cnt = k,0
#         for dun in i:
#             if pe >= dun[0]:
#                 pe -= dun[1]
#                 cnt += 1
#         result = max(result,cnt)
#     return result


# result = 0

def solution(k, dungeons):
    ln = len(dungeons)
    result = []
    visit = [0]*ln

    def dfs(val,cnt,check):
        if check == ln:
            result.append(cnt)
        else:
            for i in range(ln):
                if not visit[i]:
                    visit[i] = 1
                    if val >= dungeons[i][0]: dfs(val-dungeons[i][1],cnt+1,check+1)
                    else: dfs(val,cnt,check+1)
                    visit[i] = 0
        return
    
    dfs(k,0,0)

    return max(result)

print(solution(80,[[80,20],[50,40],[30,10]]))