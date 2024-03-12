from datetime import datetime

def solution(a, b):
    weekend = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    return weekend[(datetime(2016,a,b).weekday()+1)%7]

print(solution(1,31))
print(solution(5,24))
print(solution(2,29))