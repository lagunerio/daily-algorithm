from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split(" "))
cards = list(map(int, sys.stdin.readline().replace("\n","").split(" ")))
result = 0
for picked in combinations(cards, 3):
	three = sum(picked)
	if result<three<=m:
		result = three
print(result)
