# 백준 5430번 - AC

import sys
import json
from collections import deque

T = sys.stdin.readline()
for _ in range(int(T)):
	p = sys.stdin.readline().replace("\n", "")
	n = (sys.stdin.readline().replace("\n", ""))
	x = deque(json.loads(sys.stdin.readline().replace("\n", "")))
	front = 1
	isError = False
	for command in p:
		try:
			if command == "R":
				front *= -1
			elif command == "D" and front == 1:
				x.popleft()
			elif command == "D" and front == -1:
				x.pop()
		except:
			isError = True
			break
	x = list(map(str, x))
	if isError:
		print("error")
	elif not x:
		print("[]")
	elif x and front == -1:
		x.reverse()
		print(f"[{','.join(x)}]")
	elif x and front == 1:
		print(f"[{','.join(x)}]")