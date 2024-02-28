n = 30
d = [0] *31
def fibo (x):
    if x == 1 or x == 2:
        return 1
    if not d[x]:
        d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
print(fibo(n))  
    