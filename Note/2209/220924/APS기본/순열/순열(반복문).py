# 반복문을 사용하게 되면 고정 길이의 리스트 순열만 생성 가능


a = [1,2,3]

# 아래의 코드는 중복x 순열
for i in a:
    for j in a:
        if i == j:
            continue
        for x in a:
            if i == x or j == x:
                continue
            else:
                print(i,j,x)

# print('=='*5)
# # 아래의 코드는 중복o 순열
# for i in a:
#     for j in a:
#         for x in a:
#             print(i,j,x)