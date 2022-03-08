import sys

n = int(sys.stdin.readline())
numbers = []
for i in range(n):
	numbers.append(sys.stdin.readline())

numbers = list(map(int, numbers))
numbers.sort()
for number in numbers:
	print(number)