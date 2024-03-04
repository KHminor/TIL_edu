def solution(arr, query):
    for i,q in enumerate(query):
        if not i%2: arr = arr[:q+1]
        else: arr = arr[q:]
    return arr

print(solution([0, 1, 2, 3, 4, 5],[4, 1, 2]))