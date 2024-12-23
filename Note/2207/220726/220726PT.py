import random  # 랜덤 모듈 활용

print("================================")
print("        Battle Ship Game        ")
print("            START !!            ")
print("================================")

# 필요에 따라 추가적으로 함수를 만들어 자유롭게 활용할 수 있습니다.
# 각자의 해역에 배를 위치시키는 함수
def set_ship(index, sea):
    pass
    sea[index-1] = 1
    sea[index] = 1
    sea[index+1] = 1

    return sea
    
    
    

player_sea = [0] * 15  # 플레이어의 해역
player_attacked = [False] * 15  # 플레이어의 공격 위치 기록

computer_sea = [0] * 15  # 컴퓨터의 해역
computer_attacked = [False] * 15  # 컴퓨터의 공격 위치 기록

round = 1  # 게임 라운드

# 1. 게임 준비
while True:
    pass
    # 1-1) 플레이어의 배 시작 위치 고르기
    player_ship_position = int(input('배를 위치시킬 시작점을 고르세요: '))

    # 1-2) 범위를 벗어난 시작점을 고른 경우
    if player_ship_position > len(player_sea) or player_ship_position < 0 :
        print('-----해당 위치에는 배를 둘 수 없습니다.-----')
    else:
        break


# 1-3) 컴퓨터의 배 시작 위치를 랜덤으로 지정합니다.
com_ship_position = random.randrange(len(computer_sea))


# 1-4) 플레이어와 컴퓨터의 해역에 각각 배 위치시키기
player_sea = set_ship(player_ship_position, player_sea)   # 플레이어 해역 위치   
computer_sea = set_ship(com_ship_position, computer_sea)   # 컴퓨터 해역 위치   




# 2. 라운드 진행
print(f'''
--------------------------------------------------------------------------------------------------------------------------------
<Information Board >
플레이어의 해역: {player_sea}
플레이어의 공격 기록: {player_attacked}
--------------------------------------------------------------------------------------------------------------------------------
''')
p_cnt = 0   # 플레이어 공격 횟수
c_cnt = 0   # 컴퓨터 공격 횟수
round = 0
while True:
    pass
    
    # 2-1) 플레이어 공격
    p_attack_num = int(input("공격할 위치를 선택하세요 :"))    
    p_attack_num -= 1   # index 맞추기 위한 작업
    p_cnt += 1

    # 2-2) 플레이어의 공격 위치 선택
    if p_attack_num > len(computer_sea) or p_attack_num < 0:
        print('해역의 범위에서 벗어난 위치를 선택하였습니다. 다시 선택해 주세요.')
        continue
    elif player_attacked[p_attack_num] == True:
        print('이미 공격한 위치를 선택하였습니다. 다시 선택해 주세요.')
        continue
    
    # 2-3) 플레이어의 공격이 성공한 경우
    else:
        round += 1  # 라운드 시작
        if computer_sea[p_attack_num] == 1:
            print(f'''
<{round}라운드 결과!>
컴퓨터의 해역 : {computer_sea}
플레이어의 공격 기록 : {player_attacked}
플레이어는 컴퓨터의 해역 {p_attack_num+1}번째 칸을 공격하였고, 컴퓨터의 배는 피격되었습니다.
게임이 종료되었습니다! {round}라운드 만에 플레이어의 승리입니다!
            ''')
            break

            # 2-4) 플레이어의 공격이 실패한 경우
        elif computer_sea[p_attack_num] != 1:
            player_attacked[p_attack_num] = True 
    # 2-5) 컴퓨터의 공격 위치 지정
    # 컴퓨터가 공격하지 않은 위치를 나타내는 리스트
            

    while True:
            c_attack_num = random.randrange(len(computer_sea))
            c_attack_num -= 1   # index 맞추기 위한 작업
            if computer_attacked[c_attack_num ] != True:
                break

    p_cnt += 1

    # 2-6) 컴퓨터의 공격이 성공한 경우
    if player_sea[c_attack_num] == 1:
        print(f'''
<{round}라운드 결과!>
플레이어는 컴퓨터의 해역 {p_attack_num+1}번째 칸을 공격하였으나, 공격에 실패하였습니다!
컴퓨터는 플레이어의 해역 {c_attack_num+1}번째 칸을 공격하였고, 플레이어의 배는 피격되었습니다.
게임이 종료되었습니다! {round}라운드 만에 컴퓨터의 승리입니다!
        ''')
        break

    # 2-7) 컴퓨터의 공격이 실패한 경우
    elif player_sea[c_attack_num] != 1:
        computer_attacked[c_attack_num] = True 
        
        print(f'''
<{round}라운드 결과!>
플레이어는 컴퓨터의 해역 {p_attack_num+1}번째 칸을 공격하였으나, 공격에 실패하였습니다!
컴퓨터는 플레이어의 해역 {c_attack_num+1}번째 칸을 공격하였으나, 공격에 실패하였습니다!
        ''')

