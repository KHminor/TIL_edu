people, limit = [70, 50, 80, 50],100

people.sort()
cnt = 0
while people:
    flag = False
    for i in range(len(people)-1):
        if people[-1]+people[i] <= limit:
            if len(people):
                del people[-1]
                del people[i]
                flag = True
            elif people[-1]+people[i+1] > limit:
                del people[-1]
                del people[i]
                flag = True
            break
    if flag == False: 
        del people[-1]
    cnt += 1