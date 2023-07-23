a, b = list(map(int, input().split()))
m = [list(map(int, input().split())) for i in range()]

def func1(h, z):
    return [[sum(h[i][k] * z[k][j] for k in range(a)) % 1000 for j in range(a)] for i in range(a)]

def func2(h, q):
    if q == 1:
        return h
    
    l = func1(h, h)

    if q % 2 == 0:
        return func2(l, q//2)
    
    return func1(j(l, q//2), h)

for g in func2(m, b):
    for k in g:
        print(k % 1000, end = '')
    
    print()