def solution(targets):
    answer = 0
    targets.sort(key= lambda x: x[1])
    i = 0
    #print(targets)
    while i < len(targets):
        answer +=1
        #print(i)
        s,e = targets[i]
        j = 1
        while i+j < len(targets) and e > targets[i+j][0]:
            j +=1
        i += j
    return answer
