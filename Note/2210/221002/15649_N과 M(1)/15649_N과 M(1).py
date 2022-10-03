def nPr(s,c):
    if s == c:
        print(*li_n[0:c])
    else:
        for i in range(s,n):
            li_n[s],li_n[i] = li_n[i],li_n[s]
            nPr(s+1,c)
            li_n[s],li_n[i] = li_n[i],li_n[s]

n,c = map(int,input().split())
li_n = [i for i in range(1,n+1)]
nPr(0,c)
