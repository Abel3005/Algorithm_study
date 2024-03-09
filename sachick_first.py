def solution(arr):
    answer = -1
    #print(arr)
    s = 0
    a = []
    A = []
    s = int(arr[0])
    for i in range(1,len(arr),2):
        if arr[i] == '-':
            a.append(int(arr[i+1]))
            A.append(s)
            s = 0
        else:
            s += int(arr[i+1])
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
    for i in range(len(A)):
        if A[i] <= d[i]:
            answer += d[i]
            answer -= (a[i] + A[i])
            answer += sum(A[i+1:])
    return answer
