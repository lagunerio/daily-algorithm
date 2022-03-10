# 백준 11650번 - 좌표 정렬하기

# 풀이 1 (제출번호 40223602) : sorted 사용

import sys
from collections import defaultdict

N = sys.stdin.readline()

dots = defaultdict(list)
for _ in range(int(N)):
	x, y = map(int, sys.stdin.readline().split(" "))
	dots[x].append(y)	#여기서 바로 비교 정렬로도 해보고 비교해보자

for dot_x in sorted(dots.keys()):
	for dot_y in sorted(dots[dot_x]):
		print(f"{dot_x} {dot_y}")

# 풀이 2 (제출번호 40223925) : 비교 정렬을 직접 구현

import sys
from collections import defaultdict

N = sys.stdin.readline()

dots = defaultdict(list)
for _ in range(int(N)):
	x, y = map(int, sys.stdin.readline().split(" "))
	for idx in range(len(dots[x])):
		if dots[x][idx] > y:
			dots[x].insert(idx, y)
			break
	if y not in dots[x]:
		dots[x].append(y)

for dot_x in sorted(dots.keys()):
	for dot_y in dots[dot_x]:
		print(f"{dot_x} {dot_y}")