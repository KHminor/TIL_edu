def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)): # arr1 행
        for j in range(len(arr2[0])): # arr2 열
            for x in range(len(arr2)): # arr2 행
                answer[i][j] += arr1[i][x]*arr2[x][j]
    return answer


solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])