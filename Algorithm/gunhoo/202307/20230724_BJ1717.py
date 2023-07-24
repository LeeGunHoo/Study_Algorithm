import sys as s
s.setrecursionlimit(10 ** 6)
n, m = map(int, input().split())
l = [i for i in range(n + 1)]
def p(k):
    if l[k] == k:
        return k
    l[k] = p(l[k])
    return l[k]
for _ in range(m):
    t, a, b = map(int, s.stdin.readline().split())
    if not t and p(a) != p(b):
        l[p(a)] = p(b)
    elif t:
        print('YES') if p(a) == p(b) else print('NO')