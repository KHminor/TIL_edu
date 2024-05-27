cnt = 0
flag = True
while True:
    cnt +=1
    input_data = []
    while True:
        val = input().split('  ')
        if val == ['-1 -1']: 
            flag = False
            break
        elif val != ['']:
            input_data += val
        else: break
        
    input_data = [list(map(int,i.split())) for i in input_data][:-1]
            
    _dic = {}
    result = 'a tree.'
    for x,y in input_data[:-1]:
        try:
            if _dic[y]:
                result = 'not a tree.'
                break
        except:
            _dic[y] = x
    print("Case %d is %s"%(cnt, result))
    if not flag: break