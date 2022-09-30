year = int(input())
if year % 4 == 0 and year % 100 != 0 :
    print(f"{year}년도는 윤년입니다.")
elif year % 400 == 0:
    print(f"{year}년도는 윤년입니다.")