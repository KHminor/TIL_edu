def nPr(s,c):
    if s == c:
        pass
    else:
        for i in range(s,n):
            li_n[s],li_n[i] = li_n[i],li_n[s]
            result[s] = li_n[s]
            nPr(s+1,n)
            li_n[s], li_n[i] = li_n[i], li_n[s]
            result[s] = li_n[s]

n,c = map(int,input().split())
li_n = [i for i in range(1,n+1)]
result = [0]*c
nPr(0,c)
