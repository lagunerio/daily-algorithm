# 프로그래머스 - 코딩테스트 연습 > 2017 팁스타운 > 짝지어 제거하기
def solution(s):
	answer = -1
	stack = []

	for alpha in s:
		if not stack:
			stack.append(alpha)
		else:
			if stack[-1] == alpha:
				stack.pop()
			else:
				stack.append(alpha)	
	if stack:
		answer = 0
	else:
		answer = 1

	return answer