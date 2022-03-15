# 프로그래머스 - 코딩테스트 연습 > 월간 코드 챌린지 시즌2 > 2개 이하로 다른 비트
def solution(numbers):
	answer = []
	doubles = [2**n for n in range(1,17)]
	for number in map(int, numbers):
		if number%2==1:
			a = len(bin(number)[2:].split('0')[-1])-1
			if a==-1: a += 1
			min_fx = number + 2**a
		else:
			min_fx = number+1

		while not 1<=bin(number ^ min_fx).count('1')<=2:
			min_fx+=1
			
		answer.append(min_fx)
	return answer

print(solution([2,7]))