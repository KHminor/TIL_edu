for i in range(1,int(input())+1):
    k,n,m = map(int,input().split())
    li = [0]*(n+1)
    for j in list(map(int,input().split())): li[j] = 1

    now = n
    result = 0
    while now != 0:
        state = False
        for j in range(k,0,-1):
            if 0 >= now-j:
                now = 0
                state = True
                break
            elif li[now-j]:
                now -= j
                result += 1
                state = True
                break
        if state == False: 
            result = 0
            break
    print("#%d"%i,result)