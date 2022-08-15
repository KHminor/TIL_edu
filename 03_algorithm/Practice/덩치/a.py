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
    y_dic[y] = idx     # {185: 0, 183: 1, 186: 2, 175: 3, 155: 4}
    x_li.append(x) # [55, 58, 88, 60, 46]
    y_li.append(y) # [185, 183, 186, 175, 155]

# print(x_li,y_li) # [55, 58, 88, 60, 46] [185, 183, 186, 175, 155]

for i in range(T-1, 0, -1):
    for j in range(T-1):
        if x_li[j] > x_li[j+1]:
            x_li[j], x_li[j+1] = x_li[j+1], x_li[j]

        if y_li[j] > y_li[j+1]:
            y_li[j], y_li[j+1] = y_li[j+1], y_li[j]

# print(x_li,y_li) # [46, 55, 58, 60, 88] [155, 175, 183, 185, 186]

rank_num = best_rank = 0
cnt = 0

for num in range(T-1, 0, -1):

    if x_li[num] > x_li[num-1] and y_li[num] > y_li[num-1]: # 88 60 186 185
        print('34번줄' , x_li[num], y_li[num])
        if x_dic[x_li[num]] == y_dic[y_li[num]]:
            print('36번줄', x_dic[x_li[num]], y_dic[y_li[num]])
            if num == T-1: # 가장 큰 값에 해당 할 경우
                rank[x_li[num]] = rank_num + 1 # rank[88] = rank_num + 1 = 1
                best_rank = rank_num + 1
                print('if', num, best_rank)

            else:
                best_rank = rank.get(x_li[num+1]) + cnt
                rank[x_li[num]] = best_rank
                print('else', num, best_rank)

        else:
            print('48번줄')
            rank[x_li[num]] = best_rank+1
            cnt += 1
            print(num, cnt, best_rank)

    else:
        rank[x_li[num]] = best_rank + 1
        cnt += 1
        print(num, cnt, best_rank)

    print(rank)
