# 프로그래머스 - 코딩테스트 연습 > 2021 Dev-Matching: 웹 백엔드 개발자(상반기) > 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
	answer = []
	winning_table = {
		6: 1,
		5: 2,
		4: 3,
		3: 4,
		2: 5,
		1: 6,
		0: 6
	}
	print("=========")

	unreadable, readable = 0, []
	for lotto in lottos:
		if lotto == 0:
			unreadable += 1
		else:
			readable.append(lotto)

	match_cnt = len(win_nums) - len(set(win_nums) - set(readable))
	answer = [winning_table[match_cnt+unreadable], winning_table[match_cnt]]

	return answer


print(solution([44, 1, 0, 0, 31, 25],	[31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],	[38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35]))