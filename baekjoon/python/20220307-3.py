from itertools import combinations
import sys

n, k = map(int, sys.stdin.readline().split(" "))
things = []
for i in range(int(n)):
    things.append(list(map(int, sys.stdin.readline().split(" "))))

weights = [t[0] for t in things]
values = [t[1] for t in things]
dp = [[0 for a in range(k+1)] for b in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w = weights[i-1]
        v = values[i-1]
        if j<w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])
                
print(dp[n][k])