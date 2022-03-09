# 백준 1026번 - 보물
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().replace("\n","").split(" ")))
# b = [[i, _] for i, _ in enumerate(map(int, sys.stdin.readline().replace("\n","").split(" ")))]
b = list(map(int, sys.stdin.readline().replace("\n","").split(" ")))

s = 0
b.sort(reverse=True)
for A, B in zip(sorted(a), b):
	s += A*B

print(s)
