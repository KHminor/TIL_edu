def find_set(x):
    if x == parent[x]: return x
    else: return find_set(parent[x])

def mst():
    cnt = result = idx = 0
    while cnt < v:
        p1 = find_set(arr[idx][0])
        p2 = find_set(arr[idx][1])
        if p1 != p2:
            cnt += 1
            result += arr[idx][2]
            parent[p2] = p1         # 부모를 노드 연결
        idx += 1
        print(parent)
        print(result)
    return result

# T = int(input())
v,e = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(e)]
arr.sort(key=lambda x: x[2])
parent = [i for i in range(v+1)]
print(arr)
print(parent)

print(mst())