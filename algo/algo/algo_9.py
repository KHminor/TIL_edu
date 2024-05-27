# def solution(elements):
#     dic, ln = {i:0 for i in range(sum(elements)+1)}, len(elements)
#     elements_double = elements*2
#     for i in range(1, ln+1):
#         for j in range(ln): 
#             if not dic[sum(elements_double[j:j+i])]: dic[sum(elements_double[j:j+i])] = sum(elements_double[j:j+i])
#     return len([ i for i in list(dic.values()) if i != 0])


def solution(elements):
    dic, ln = {i:0 for i in range(sum(elements)+1)}, len(elements)
    for i in range(ln):
        hap = elements[i]
        dic[hap] = hap
        for j in range(i+1, i+ln):
            hap += elements[j%ln]
            if not dic[hap]: dic[hap] = hap            
    return len([ i for i in list(dic.values()) if i != 0])

solution([7,9,1,1,4])
