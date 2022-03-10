# 백준 10816 - 숫자 카드 2
import sys
from collections import defaultdict

N = sys.stdin.readline()
cards = sys.stdin.readline().replace("\n","").split(" ")
card_count = defaultdict(int)
for number in cards:
	card_count[number] += 1

M = sys.stdin.readline()
xs = sys.stdin.readline().replace("\n","").split(" ")

result = list(map(str, [card_count[_] for _ in xs]))
print(" ".join(result))