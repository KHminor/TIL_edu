# def solution(arr):
#     li = []
#     for i in range(len(arr)):
#         if i != len(arr)-1: 
#             if arr[i] != arr[i+1]: li.append(arr[i])
#         else:li.append(arr[i])
#     return li

# print(solution([1,1,3,3,0,1,1]))

def solution(arr):
    li = []
    [li.append(i) for i in arr if li[-1:] != [i]]
    return li

print(solution([1,1,3,3,0,1,1]))