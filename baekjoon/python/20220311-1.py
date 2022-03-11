# 백준 1158 - 요세푸스 문제
import sys

N, K = map(int, sys.stdin.readline().replace("\n","").split(" "))
circle = [_ for _ in range(1, N+1)]

towel = K-1
result = []
while circle:
	result.append(circle.pop(towel))
	towel += K-1
	if not towel == 0 and circle:
		towel %= len(circle)
print(f"<{', '.join(map(str, result))}>")