# 백준 10866번 - 덱
import sys
from collections import deque

class DEQUE:
	def __init__(self, q):
		self.q = deque(q)

	def push_front(self, x):
		self.q.appendleft(x)

	def push_back(self, x):
		self.q.append(x)

	def pop_front(self):
		try:
			print(self.q.popleft())
		except:
			print(-1)

	def pop_back(self):
		try:
			print(self.q.pop())
		except:
			print(-1)

	def size(self):
		print(len(self.q))

	def empty(self):
		if self.q:
			print(0)
		else:
			print(1)

	def front(self):
		if self.q:
			print(list(self.q)[0])
		else:
			print(-1)

	def back(self):
		if self.q:
			print(list(self.q)[-1])
		else:
			print(-1)

N = sys.stdin.readline()
deq = DEQUE([])
for _ in range(int(N)):
	commands = sys.stdin.readline().replace("\n","").split(" ")
	if commands[0] == "push_front":
		deq.push_front(commands[1])
	elif commands[0] == "push_back":
		deq.push_back(commands[1])
	elif commands[0] == "pop_front":
		deq.pop_front()
	elif commands[0] == "pop_back":
		deq.pop_back()
	elif commands[0] == "size":
		deq.size()
	elif commands[0] == "empty":
		deq.empty()
	elif commands[0] == "front":
		deq.front()
	elif commands[0] == "back":
		deq.back()
	