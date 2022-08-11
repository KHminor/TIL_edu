import sys
sys.stdin = open('input.txt')

for t in range(10):
    dump=int(input())
    boxs=list(map(int,input().split()))
    for i in range(len(boxs)-1,0,-1):
        for j in range(0,i):
            if boxs[j]>boxs[j+1]:
                boxs[j],boxs[j+1]=boxs[j+1],boxs[j]
    min_v=boxs[0]
    max_v=boxs[-1]
    count=0

    while count<dump:
        for bx in range(0,len(boxs)):
            if min_v<boxs[bx]:
                boxs[bx-1]+=1
                break
        for bx in range(len(boxs)-1,0,-1):
            if max_v>boxs[bx]:
                boxs[bx+1]-=1
                break
        min_v = boxs[0]
        max_v = boxs[-1]
        count+=1

    print(f'#{t+1} {max_v-min_v}')