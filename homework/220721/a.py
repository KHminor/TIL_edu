# import random

# is_playing = True

# while is_playing:
#     print('================================')
#     print('        Up and Down Game        ')
#     print('================================')

#     answer = random.randint(1, 10000)  # 1이상 10000이하의 난수  
#     counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

#     # 여기부터 코드를 작성하세요.


#     while True:
#         counts += 1

#         num = int(input("1 이상 10000 이하의 숫자를 입력하세요. :"))    

#         if 1 > num > 10000 :
#             print("잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.")
#             continue

#         if answer == num:
#             print(f"Correct!!! {counts}회 만에 정답을 맞히셨습니다.")
#             is_playing = False

#         elif answer > num:
#             print("Up!!!")
#             continue
        
#         else:
#             print("Down!!!")
#             continue
    
#         start_end = input("게임을 재시작하시려면 y, 종료하시려면 n을 입력하세요. :")
        
#         if start_end == 'n':
#             print("이용해주셔서 감사합니다. 게임을 종료합니다.")
#             break

#         elif start_end != 'y' and 'n':
#             print("잘못된 값을 입력하셨습니다. 게임을 종료합니다. ")  
#             break
#     break




# =================================================================================


print('=================================')
print('         Vending Machine         ')
print('=================================')
print('[Menu]')
print('1. 콜라 500원')
print('2. 사이다 700원')
print('3. 레모네이드 4500원')
print('4. 오렌지주스 2000원')
print('5. 초코우유 1200원')
print('6. 아메리카노 3600원')
print('=================================')

menus = ['콜라', '사이다', '레모네이드', '오렌지주스', '초코우유', '아메리카노']  # 메뉴 이름
costs = [500, 700, 4500, 2000, 1200, 3600]  # 메뉴 가격
budget = 0  # 자판기에 넣은 총 누적 금액


while True:
    print()
    money = int(input('금액을 넣어주세요.(그만 넣으시려면 0을 입력하세요.) : '))

    # 여기부터 코드를 작성하세요.

    menus_num = list(range(1,len(menus)+1))
    
    index_menus = dict(zip(menus_num, menus))
    index_cost = dict(zip(menus_num, costs))
    dic = dict(zip(menus, costs))

    low_cost = min(costs) 

    if money >= 1:
        budget += money
        print(f"현재 누적 금액은 {budget}원입니다.")
        continue

    elif money < 0:
        print("금액은 1원 이상 넣어주세요.")
        continue
    
    elif money == 0:
        if budget < low_cost:
            print(f"{budget}원으로 구매 가능한 메뉴가 없습니다. ")
            break

        elif budget > low_cost:
            for i, j in index_menus.items():     # i = index, j = menus
                if budget >= dic[j]:
                    print(f"{i}. {j} {dic[j]}원")

            while True:
                buy_num = int(input("구매하실 메뉴의 번호를 입력하세요. ")) 
                if buy_num in menus_num:                   
                    if budget >= index_cost[buy_num]:
                        print(f"{index_menus[buy_num]}를 구매하셨습니다.")
                        print(f"거스름돈은 {budget - (index_cost[buy_num])}원 입니다. 감사합니다.")
                        break
                    
                    elif budget < index_cost[buy_num]:
                        print("구매할 수 없는 메뉴입니다.")
                        continue

                elif buy_num not in menus_num :
                    print("구매할 수 없는 메뉴입니다.")
                    continue
    break