# 프로그래머스 - 코딩테스트 연습 > Summer/Winter Coding(2019) > 멀쩡한 사각형
from math import gcd

def solution(w,h):
	answer = 1
	
	wh_gcd = gcd(w, h)
	min_x, min_y = w//wh_gcd, h//wh_gcd
	
	min_cutted = min_x + min_y - 1

	answer = (w * h) - (min_cutted * wh_gcd)
	return answer

print(solution(8,12))