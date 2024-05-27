# 화물의 무게와 트럭 적재용량을 내림 차순 정렬 후 추가된 개수만큼 idx를 증가시키며 찾기

for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    w_li = sorted(list(map(int,input().split())), reverse=True) # 화물 무게
    t_li = sorted(list(map(int,input().split())), reverse=True) # 트럭 적재 용량
    cnt, hap = 0, 0 # 적재된 횟수
    for i in range(n):
        if t_li[cnt]>=w_li[i]: cnt, hap = cnt +1, hap+w_li[i]
        if cnt == m: break
    print('#%d'%tc, end=' ')
    print(hap)