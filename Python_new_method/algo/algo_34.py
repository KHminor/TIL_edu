# def solution(want, number, discount):
#     result_dict, _range, result = {i:j for i,j in zip(want, number)}, sum(number), 0
#     for i in range(len(discount)-_range+1):
#         want_dict = {i:0 for i in want}
#         for j in range(_range):
#             try: want_dict[discount[i+j]] += 1
#             except: break
#         if want_dict == result_dict: result += 1
#     return result


# print(solution(
#     ["apple"], 
#     [10], 
#     ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
#     ))
a = [1,2,3,4,5]
for i in range(5-2): print(i)