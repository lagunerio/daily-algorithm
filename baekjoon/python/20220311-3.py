# 백준 6603번 - 로또
import sys
from itertools import combinations

round = 0
testcase = sys.stdin.readline().replace("\n","").split(" ")
k = testcase.pop(0)
while True:
	if k == "0":
		break
	else:
		if not round == 0:
			print("\n")
		combis = combinations([_ for _ in range(int(k))], 6)
		for c in combis:
			print(" ".join([testcase[_] for _ in c]))
		testcase = sys.stdin.readline().replace("\n","").split(" ")
		k = testcase.pop(0)
	round += 1