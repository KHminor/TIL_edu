# n, m = map(int, input().split())
# cnt, hap = 0, 0
# 이것도 내가 스스로 못품...
# 다시 풀어보기
# print('0 1')




# # 리프의 개수
# leaf = 0
# if m == 2:
#     leaf = 1  # 중심 노드를 리프로 포함
# li = []
# last_leaf = 0
# for i in range(1, n):
#     if m > leaf:
#         li.append([0, i])
#         leaf += 1
#     else:
#         li.append([last_leaf, i])
#     last_leaf = i
# print(li)

# n, m = map(int, input().split())
# li = []
# if m == 2:
#     for i in range(n - 1):
#         li.append([i, i + 1])

# else: # m이 3 이상
#     li.append([0,1])
#     for i in range(2, m + 1):
#         li.append([1, i])
#     for j in range(m, n - 1):
#         li.append([j, j + 1])

# print(li)