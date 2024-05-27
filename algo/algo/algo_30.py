# def solution(arr1, arr2):
#     ln1, ln2 = len(arr1), len(arr1[0])
#     li = [[0 for i in range(ln2)] for i in range(ln1)]
#     for i in range(ln1):
#         for j in range(ln2):
#             li[i][j] = arr1[i][j] + arr2[i][j]
#     return li

def xx(a): 
    return a

def solution(A,B):
    # return [list(map(sum, zip(*x))) for x in zip(A, B)]
    # print([list(map(sum,zip(*i))) for i in zip(A,B)])
    # print([[ (x,y) for x,y in zip(a,b)] for a,b in zip(A,B)])
    print([i for i in zip(A,B)])
    print([list(map(xx,zip(*i))) for i in zip(A,B)])
    return 


solution([[1,2],[2,3],[3,4,5]]	, [[3,4],[5,6],[4,5,6]])