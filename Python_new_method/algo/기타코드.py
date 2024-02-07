from itertools import permutations
def find(start,cnt,):
    global n,m,result,now,val
    if cnt == m: 
        val.sort()
        if result == -1: result = val[-1]-val[0]
        else: result = min(result, val[-1]-val[0])
        return
    for k in range(start,n):
        check = dic[now[cnt]] - dic[guitar[k]] if dic[now[cnt]] - dic[guitar[k]] >= 0 else 12 + dic[now[cnt]] - dic[guitar[k]]
        if check == 0: continue
        val[cnt] = check
        find(k+1,cnt+1)

dic = {
    "A":1, "A#":2, "B":3, "C":4, "C#":5, "D":6, "D#":7, "E":8, "F":9, "F#":10, "G":11, "G#":12
}
n,m = map(int,input().split())
guitar = list(input().split())
chord = list(input().split())
now = []
val = [0,0,0]
result = -1
for i in list(permutations(chord,m)):
    now = list(i)
    find(0,0)
print(result)