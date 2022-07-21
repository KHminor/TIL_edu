# def my_all(elements):
    # 넘겨받은 elements가 모두 순회를 해야한다. (반복)
    # 참인지 아닌지 확인 해야한다 (조건)

    # 최종 반환 값
    # result = True

    # for ele in elements:
    #     # if bool(ele) == False:
    #     # if not bool(ele)
    #     if bool(ele) == False: 
    #         if not ele:
    #             # result = False
    #             # break
    #             return False

    # 값이 비어 있을때는 True 를 반환 하는 것.
    # 안해도 된다. 
    # 비어있는 값을 반복문에 넣을 경우 반복문이 돌지 않기 떄문.

    # return True


# 함수 내에서 여러개의 반복문이 있을 경우 return False 를 하면 
# break 는 한번의 반복문만 빠져나오지만 
# return False를 하면 함수의 return 값이 생기기에 함수 자체가 끝이 난다.



#any

# def my_any(elements):
#     for ele in elements:
#         if ele:
#             return True
#         return False

# def sum_of_digit(number):
#     result = 0

#     # 언제까지 -> number / 10 -> 10 False가 될 때 까지.
#     while number / 10:
#         # 나머지를 분리해내서 result에 더하기
#         result += number % 10
#         number = number // 10
#     return result


# 재귀 함수는 규칙적으로 바뀔때 사용.

def sum_of_digit(number):
    # 종료 조건
    if number < 10:
        return number
    else:
        namuji = number % 10

    return namuji + sum_of_digit(number // 10)