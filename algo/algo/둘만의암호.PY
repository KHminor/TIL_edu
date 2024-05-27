def solution(s, skip, index):
    result = []
    s_skip = set(skip)
    for i in s:
        check = 0
        i_ord = ord(i)
        while check != index:
            n_i_ord = i_ord+1 if 122 >= i_ord+1 else 96+(i_ord+1)%122
            if chr(n_i_ord) not in s_skip: check += 1
            i_ord = n_i_ord
        result.append(chr(i_ord))
    return "".join(result)

print(solution("z","wbqd",5))