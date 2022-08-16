T = int(input())
x_dic = {}
y_dic = {}
rank = {}
x_li = []
y_li = []
for idx in range(T):
    x,y = map(int,input().split())
    rank[x] = 0      # {55: 0, 58: 0, 88: 0, 60: 0, 46: 0}

    x_dic[x] = idx     # {55: 0, 58: 1, 88: 2, 60: 3, 46: 4}
    y_dic[idx] = y     # {0: 185, 1: 183, 2: 186, 3: 175, 4: 155}
    x_li.append(x) # [55, 58, 88, 60, 46]
    y_li.append(y) # [185, 183, 186, 175, 155]

# print(y_dic.get(x_dic.get(55))) # 185
# print(y_dic.get(x_dic.get(88))) # 186

# print(x_li,y_li) # [55, 58, 88, 60, 46] [185, 183, 186, 175, 155]

for i in range(T-1, 0, -1):  # x_li와 y_li를 버블 정렬
    for j in range(T-1):
        if x_li[j] > x_li[j+1]:
            x_li[j], x_li[j+1] = x_li[j+1], x_li[j]

        if y_li[j] > y_li[j+1]:
            y_li[j], y_li[j+1] = y_li[j+1], y_li[j]

# print(x_li,y_li) # [46, 55, 58, 60, 88] [155, 175, 183, 185, 186]

best_rank = 0  # 서로 값이 다른 경우 전의 rank 를 사용하기 위한 용도
cnt = 1  # 서로 비교가 되지 않는 값들의 경우 cnt += 1 하기위한 용도

for num in range(T-1, 0, -1):
    # x_li의 num 에 해당 하는 값을 x_dic에 넣어 value를 가져와
    # 해당 value를 y_dic에 넣어 value를 찾아 그것과 y_li[num]의 값과 동일 한지 확인
    if y_dic.get(x_dic.get(x_li[num])) == y_li[num]:  # 4, 2
        # x_li를 통해서 다음의 num의 y 값과 비교하여 클 경우
        if y_dic.get(x_dic.get(x_li[num])) > y_dic.get(x_dic.get(x_li[num-1])):
            rank[x_li[num]] = best_rank + cnt
            best_rank += 1
            cnt = 1

        # 크지 않을 경우 # x = 58  y = 183 , x = 55  y = 185
        elif y_dic.get(x_dic.get(x_li[num])) < y_dic.get(x_dic.get(x_li[num-1])):
            rank[x_li[num]] = best_rank + 1
            cnt += 1


    else:  # 값이 같지 않은 경우

        rank[x_li[num]] = best_rank + 1
        cnt += 1


if y_dic.get(x_dic.get(x_li[0])) == y_li[0]:
    rank[x_li[0]] = best_rank + cnt
else:
    rank[x_li[0]] = best_rank + 1

print(*(list(rank.values())))

# 현재 케이스에서는 답이 나오는데 다른 케이스들을 확인해봐야 함
# 예를 들어 가장 x_li의 가장 큰 값과 y_li의 가장 큰 값이 다를 때부터