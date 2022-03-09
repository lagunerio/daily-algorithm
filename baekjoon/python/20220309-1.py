# 백준 10989번 - 수 정렬하기 3

import sys
from collections import defaultdict

n = sys.stdin.readline()
numbers = defaultdict(int)
for i in range(int(n)):
	numbers[int(sys.stdin.readline())] += 1

for key in sorted(list(numbers.keys())):
	for _ in range(numbers[key]):
		print(key)