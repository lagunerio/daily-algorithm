# 프로그래머스 - 코딩테스트 연습 > 2021 Dev-Matching: 웹 백엔드 개발자(상반기) > 다단계 칫솔 판매
from collections import defaultdict

def solution(enroll, referral, seller, amount):
	answer = []

	hiererchy = dict()
	for enr, ref in zip(enroll, referral):
		hiererchy[enr] = ref

	result = defaultdict(int)
	for s, a in zip(seller, amount):
		# result[s] += a * 100
		earn = a * 100
		enroller, fee, add = "", 10, 0
		while fee>9 and not s == "-":
			enroller = hiererchy[s]
			fee = earn // 10
			result[s] += earn - fee
			s = enroller
			earn = fee
		result[s] += earn

	for enr in enroll:
		answer.append(result[enr])

	answer = list(map(int, answer))
	return answer