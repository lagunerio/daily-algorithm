# 프로그래머스 - 코딩테스트 연습 > 월간 코드 챌린지 시즌2 > 괄호 회전하기
from collections import deque

def solution(s):
	answer = 0
	close_type = {
		"(": 1,
		")": -1,
		"[": 10,
		"]": -10,
		"{": 100,
		"}": -100
	}
	
	for x in range(len(s)):
		new_s = list(s[x:] + s[:x])
		stack = deque([])
		possible = 1
		while new_s and possible:
			n = new_s.pop(0)
			if close_type[n] > 0:
				stack.append(n)
			elif not stack:
				possible = 0
			else:
				last = stack.pop()
				if not close_type[n]+close_type[last] == 0:
					possible = 0
		if possible and not stack:
			answer += possible
					
	return answer