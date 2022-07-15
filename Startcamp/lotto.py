# 1. lotto api로 부터 데이터 받아오기

# 2. 지난주 당첨 번호 알아내기 (1등만)

# 3. random module 이 가지고 있는 sample 이라는 함수를 사용하여 1부터 45중에 무작위 6개를 뽑기

# 4. 뽑은 번호가 당첨 번호와 일치하는지 확인한다.

# 5. (도전과제) 천번 이상 새로운 로또 번호를 생성하여서 매번 당첨이 되었는지 확인해 보는 로직 작성

# 6. (도전과제) 1등부터 2등을 포함한 (보너스 번호까지) 4등까지의 각 당첨 횟수 출력하기.


# 1번 과제

# import requests
# url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
# response = requests.get(url).json
# print(response)
# ===========================================================

# 2번 과제
# import random
# num = range(1,46)
# print(random.sample(num, 6))
# ===========================================================

# 3번 과제
# import requests

# num = input("회차번호: ")
# # url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1023'
# url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={}'.format(num)
# response = requests.get(url).json()
# drwtNo1 = response["drwtNo1"]
# drwtNo2 = response["drwtNo2"]
# drwtNo3 = response["drwtNo3"]
# drwtNo4 = response["drwtNo4"]
# drwtNo5 = response["drwtNo5"]
# drwtNo6 = response["drwtNo6"]
# print(drwtNo1,drwtNo2,drwtNo3,drwtNo4,drwtNo5,drwtNo6)

# 4. 뽑은 번호가 당첨 번호와 일치하는지 확인한다.

# [9, 11, 37, 44, 24, 10]
# 회차번호: 1023
# 10 14 16 18 29 35

# 5. (도전과제) 천번 이상 새로운 로또 번호를 생성하여서 매번 당첨이 되었는지 확인해 보는 로직 작성

# import requests
# import random

# num = input("회차번호: ")
# url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={}'.format(num)
# response = requests.get(url).json()
# drwtNo1 = response["drwtNo1"]
# drwtNo2 = response["drwtNo2"]
# drwtNo3 = response["drwtNo3"]
# drwtNo4 = response["drwtNo4"]
# drwtNo5 = response["drwtNo5"]
# drwtNo6 = response["drwtNo6"]
# li = [drwtNo1,drwtNo2,drwtNo3,drwtNo4,drwtNo5,drwtNo6]
# li.sort()
# print("금주차 {}의 로또 번호는 {} 입니다.".format(num,li))



# a = 0
# cnt = 0
# while True :
#     a += 1
#     num_range = range(1,46)
#     lucky = random.sample(num_range, 6)
#     lucky.sort()
#     if li == lucky:
#         print("해당 번호 {}는 당첨되었습니다.".format(lucky))
#         cnt += 1
#     else:
#         print(lucky)
#     if a >= 1000:
#         if cnt >= 1:
#             print("{}회 로또에 당첨된 횟수는 {}번 입니다.".format(num,cnt))
#         else:    
#             print("{}회 로또에 당첨되지 못했습니다.".format(num))
#         # print(a)
#         break

# 6. (도전과제) 1등부터 2등을 포함한 (보너스 번호까지) 4등까지의 각 당첨 횟수 출력하기.

# import requests
# import random

# num = input("회차번호: ")
# url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={}'.format(num)
# response = requests.get(url).json()
# drwtNo1 = response["drwtNo1"]
# drwtNo2 = response["drwtNo2"]
# drwtNo3 = response["drwtNo3"]
# drwtNo4 = response["drwtNo4"]
# drwtNo5 = response["drwtNo5"]
# drwtNo6 = response["drwtNo6"]
# li = [drwtNo1,drwtNo2,drwtNo3,drwtNo4,drwtNo5,drwtNo6]
# li.sort()
# print("금주차 {}의 로또 번호는 {} 입니다.".format(num,li))



# a = 0
# cnt = 0
# while True :
#     a += 1
#     num_range = range(1,46)
#     lucky = random.sample(num_range, 6)
#     lucky.sort()
#     if li == lucky:
#         print("해당 번호 {}는 당첨되었습니다.".format(lucky))
#         cnt += 1
#     else:
#         print(lucky)
#     if a >= 1000:
#         if cnt >= 1:
#             print("{}회 로또에 당첨된 횟수는 {}번 입니다.".format(num,cnt))
#         else:    
#             print("{}회 로또에 당첨되지 못했습니다.".format(num))
#         # print(a)
#         break
    


li = [1,2,3,4,5,6]
li2 = [4,5,6,7,8,9]
l_num = 0
correct = []
for i in range(len(li)):
    for y in range(len(li2)):
        if li[i] == li2[y]:
            correct.append()