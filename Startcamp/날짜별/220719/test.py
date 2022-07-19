# cola = 500
# cider = 700
# Lemonade = 4500
# Orange_juice = 2000
# chocolate_milk = 1200
# Americano = 3600

# ================================================================

# # 3만원 소지 콜라 사이다 2개씩 , 나머지 메뉴는 1개씩 구매후 잔액.
# money = 30000
# change = 0
# change = money - (cider*2 + cola*2 + Lemonade + Orange_juice + chocolate_milk + Americano) 
# print(change)

# ================================================================

# port = [False,False,False,True,False,False,False,True,True,False,False,False,False,False,True]
# print(port[:])

# ================================================================

# odd_ports = port[::2]
# print(odd_ports)

# ================================================================

# ssafy_choice = {1, 12, 27, 33, 38, 42}
# lucky_numbers = {7, 15, 27, 33, 37, 42}
# count = ssafy_choice .intersection(lucky_numbers)
# print(count)

# ================================================================
# n = int(input("몇개의 도시를 추가할건지 작성해주세요: "))
# air_info = []
# for i in range(n) :
#     name = input("도시 이름을 입력하세요: ")
#     capital = str(input("수도 여부를 입력하세요: "))
#     o2, co2 = map(int,input("산소 농도와 이산화탄소 농도를 입력하세요: ").split())
#     print(f"도시 이름은 {name}이며, {capital}. 산소 농도는 {o2}이며, 이산화탄소 농도는 {co2}입니다.")
#     air_status = {o2: co2}
#     air_info.append({name: air_status})

# print(air_info)

# ================================================================

n = int(input("몇개의 도시를 추가할건지 작성해주세요: "))
air_info = []
O2_info = []
for i in range(n) :
    name = input("도시 이름을 입력하세요: ")
    capital = str(input("수도 여부를 입력하세요: "))
    o2, co2 = map(int,input("산소 농도와 이산화탄소 농도를 입력하세요: ").split())
    print(f"도시 이름은 {name}이며, {capital}. 산소 농도는 {o2}이며, 이산화탄소 농도는 {co2}입니다.")
    O2_info.append(o2)
    air_status = {o2: co2}
    air_info.append({name: air_status})

print(O2_info)