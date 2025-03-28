from collections import deque

# def solution(cacheSize, cities):
#     if cacheSize == 0: return len(cities)*5 

#     cities = [ i.upper() for i in cities]
#     result, cache_li = 0, deque(['']*cacheSize)
#     for i in range(len(cities)//cacheSize):
#         for j in range(cacheSize):
#             if cache_li[j] == '': 
#                 result += 5
#                 cache_li[j] = cities[(i*cacheSize)+j] # 빈칸의 경우 추가해주면서 +5 해주기
#             else:
#                 if cities[(i*cacheSize)+j] in cache_li: # 지역이 존재할 경우 가장 앞에 있는 값을 맨 뒤로 보내면서 +1 해주기
#                     del cache_li[cache_li.index(cities[(i*cacheSize)+j])]
#                     cache_li.append(cities[(i*cacheSize)+j])
#                     result += 1
#                 else: # 없다면
#                     result += 5
#                     cache_li.rotate(-1)
#                     cache_li[-1] = cities[(i*cacheSize)+j]

#     return result


# def solution(cacheSize, cities):
#     if cacheSize == 0: return len(cities)*5 

#     cities = [ i.upper() for i in cities]
#     result, cnt, cnt_idx, cache_li = 0, 0, 0, deque()

#     while cnt < len(cities):

#         if cities[cnt] in cache_li: # 지역이 존재할 경우 해당 값에 해당하는 index를 제거 후 맨 뒤에 새로 추가해주면서 +1 해주기
#             del cache_li[cache_li.index(cities[cnt])]
#             cache_li.append(cities[cnt])
#             result += 1
#         else: 
#             # 없다면 +5 해주면서 cacheSize 크기만큼 추가되지 않았다면 추가하고, 
#             # 꽉 찼다면 deque의 rotate를 사용해서 회전 시킨 다음 가장 마지만 index 값을 새롭게 교체하기. 
#             result += 5
#             if len(cache_li) < cacheSize:
#                 cache_li.append(cities[cnt])
#             else:
#                 cache_li.rotate(-1)
#                 cache_li[-1] = cities[cnt]
#         cnt, cnt_idx = cnt+1, cnt_idx+1
#         if cnt_idx == cacheSize: cnt_idx %= cacheSize

#     return result

def solution(cacheSize, cities):
    if cacheSize == 0: return len(cities)*5 

    cities = [ i.upper() for i in cities]
    result, cnt, cnt_idx, cache_li = 0, 0, 0, deque(maxlen=cacheSize)

    while cnt < len(cities):
        if cities[cnt] in cache_li: # 지역이 존재할 경우 가장 앞에 있는 값을 맨 뒤로 보내면서 +1 해주기
            del cache_li[cache_li.index(cities[cnt])]
            cache_li.append(cities[cnt])
            result += 1
        else: 
            # 없다면 +5 해주면서 cacheSize 크기만큼 추가되지 않았다면 추가하고, 
            # 꽉 찼다면 maxlen을 활용해 추가해주면서 자연스럽게 가장 앞 index가 사라지면서 
			# 맨 뒤 index로 새롭게 추가되도록 하기. 
            result += 5
            cache_li.append(cities[cnt])
            
        cnt, cnt_idx = cnt+1, cnt_idx+1
        if cnt_idx == cacheSize: cnt_idx %= cacheSize

    return result

print(solution(4, ["Jeju", "Pangyo", "NewYork", "newyork"]))

# a = [1,2,3,4]
# print(a.index(3))
