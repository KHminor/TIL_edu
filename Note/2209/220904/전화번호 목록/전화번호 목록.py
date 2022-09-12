def solution(phone_book):
    cnt = 0
    while cnt != len(phone_book):
        b = phone_book[:]
        ch_s = b.pop(cnt)
        ln = len(ch_s)
        for i in b:
            if len(ch_s) > len(i):
                continue
            for j in range(len(i) - len(ch_s) + 1):
                if ch_s == i[j:ln]:
                    return False

        cnt += 1
    return True






# phone_book = list(input().split())
# phone_book = (*phone_book)
# print(solution(phone_book))
