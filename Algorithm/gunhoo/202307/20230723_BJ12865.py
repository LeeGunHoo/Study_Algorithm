n, k = map(int, input().split())

dp = (k + 5) * [0]

for _ in range(n):
    w, v = map(int, input().split())
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i], dp[i-w] + v)

print(dp[k])