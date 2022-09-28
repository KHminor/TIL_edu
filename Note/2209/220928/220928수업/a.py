def find_set(v):
    while tree[v] != v:
        v = tree[v]
    return v

def union(a,b):
    r1 = find_set(a)
    r2 = find_set(b)
    tree[r2] = tree[r1]

