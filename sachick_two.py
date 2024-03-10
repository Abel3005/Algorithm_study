def solution(arr):
    answer = -1
    #print(arr)
    s = 0
    a = []
    A = []
    s = int(arr[0])
    ff = True
    for i in range(1,len(arr),2):
        if arr[i] == '-':
            a.append(int(arr[i+1]))
            A.append(s)
            ff = False
            s = 0
        else:
            s += int(arr[i+1])
    #-연산이 하나도 없을 경우
    if ff:
        return s
    s = 0
    d = []
    t = a[1:]
    for i in t[::-1]:
        s += i
        # an, an + an1- , ...
        d.append(s)
    d.reverse()
    answer = A[0]
    A = A[1:]
    print(a)
    print(A)
    print(d)
    if len(a) == 1 and len(A) == 0:
        answer -= a[0]
        return answer
    f = True
    for i in range(len(A)-1):
        if A[i] < a[i+1]:
            answer += d[i]
            answer -= (a[i] + A[i])
            answer += sum(A[i+1:])
            f=False
            break
        else:
            answer += (-a[i] + A[i])
    if f:
        if len(A)< len(a):
            if A[len(A)-1] < a[len(a)-1]:
                answer += a[len(a)-1]
                answer -= (a[len(a)-2] + A[len(A)-1])
            else:
                answer -= (a[len(a)-2] + a[len(a)-1])
                answer += A[len(A)-1]
        else:
            answer += (-a[len(a)-1] +A[len(A)-1])
    return answer
