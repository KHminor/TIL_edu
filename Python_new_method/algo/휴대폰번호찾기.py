def makeDict(number):
    dic = {str(i):0 for i in range(10)}
    for i in number:
        if i == "-": continue
        else: dic[i] += 1
    return dic

def find(ans, you_dict):
    cnt = 0
    idx = 0
    for i in ans:
        if i == str(you_dict[str(idx)]): cnt += 1
        idx += 1
    return cnt

print("어서오세요 :)")
you = "010-1234-5678"
you_dict = makeDict(you)
me = input("본인의 번호를 입력해주세요! : ")
me_dict = makeDict(me)
while True:
    isState = True
    print("상대방의 휴대번호가 0~9까지 몇개씩 있는지 맞춰보세요!")
    print("ex)010-0000-1101 -> 입력: 740000000")
    ans = input()
    result = find(ans, you_dict)
    if result == 10: 
        print("정확해요!")
        print("상대방의 번호는: %s"%you)
        break
    else:
        print("아쉽지만 %d개 맞추셨어요ㅠ"%result)
        while True:
            isCon = input("다시 도전하신다면 yes, 그만하겠다면 no를 입력해주세요! : ")
            if isCon in ["yes", "YES", "Yes"]: break
            elif isCon in ["no", "NO", "No"]: 
                isState = False
                break
            else: 
                print("다시 입력해주세요")
                continue
    if not isState: break