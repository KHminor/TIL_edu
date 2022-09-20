# # bfs - q 사용
    # visited = [0]*(N+1)
    # ch2[v2].sort()
    # q = ch2[v2]
    # visited[v2] = 1
    # result2 = [v2]
    # num = []
    # while q:
    #     v2 = q.pop(0)
    #     if visited[v2] == 0:
    #         result2.append(v2)
    #         for i in range(len(ch2[v2])):
    #             if ch2[v2][i] != 0 :
    #                 num.append(ch2[v2][i])
    #                 num.sort()
    #         for j in num:
    #             q.append(j)
    #     visited[v2] = 1
    # print(*result2)
    #