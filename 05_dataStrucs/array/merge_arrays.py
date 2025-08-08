def array_merge(arra1, arra2):
    res=[]

    arra1_len = len(arra1)
    arra2_len = len(arra2)

    i = 0
    j = 0

    while True:
        if i == arra1_len and j == arra2_len:
            break
        elif i == arra1_len:
            res.append(arra2[j])
            j += 1
        elif j == arra2_len:
            res.append(arra1[i])
            i += 1
        elif arra2[j] <= arra1[i]:
            res.append(arra2[j])
            j += 1
        elif arra1[i] < arra2[j]:
            res.append(arra1[i])
            i += 1
            
    print(res)
    return res

array_merge([2,4,5,5,6,7,8],[2,3,22,33])