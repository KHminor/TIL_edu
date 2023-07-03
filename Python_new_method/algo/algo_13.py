from math import prod

def solution(clothes):
    dic = {}
    for i in clothes:
        try: dic[i[1]] += 1
        except: dic[i[1]] = 1
        
    li = [i+1 for i in list(dic.values())]
    return prod(li)-1

# def solution(clothes):
#     _dict = {k:[] for _,k in clothes}
#     for v, k in clothes:
#         _dict[k].append(v)
#     print(_dict.values())
#     res = 1
#     for v in _dict.values():
#         res *= (len(v) + 1)
#     return res - 1

print(solution([["yellow_hat", "headgear"], ["green_turban", "headgear"], ["blue_sunglasses", "eyewear"], ["red_sunglasses", "eyewear"], ["blue_pant", "underwear"], ["red_pant", "underwear"],]))
# print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))