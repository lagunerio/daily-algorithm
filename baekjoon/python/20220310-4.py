# 백준 1966번 - 프린터 큐
import sys
from collections import deque

test_cases = sys.stdin.readline().replace("\n", "")
for _ in range(int(test_cases)):
	N, M = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))
	printer_queue = list(map(int, sys.stdin.readline().replace("\n", "").split(" ")))
	whos_turn, first_turn = 0, sorted(printer_queue)[-1]
	printed = 0

	while printer_queue[M] > 0:

		if printer_queue[whos_turn]<first_turn:
			whos_turn+=1
		elif printer_queue[whos_turn] == first_turn:
			printed+=1
			printer_queue[whos_turn] = 0
			first_turn = sorted(printer_queue)[-1]
			whos_turn+=1

		whos_turn%=N

	print(printed)