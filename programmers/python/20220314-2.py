# 프로그래머스 - 코딩테스트 연습 > 2020 KAKAO BLIND RECRUITMENT > 문자열 압축
def zipper(blocks, block_str, count=1):
	if len(blocks) < 1:
		return blocks, count

	if blocks[0] == block_str:
		blocks, count = zipper(blocks[1:], block_str, count+1)
	
	return blocks, count

def solution(s):
	answer = len_s = len(s)
	for block_len in range(1, len_s//2+1):
		whats_left = ""
		blocks = [s[idx*block_len:idx*block_len+block_len] for idx in range(len_s//block_len)]
		if len_s%block_len > 0:
			whats_left = s[(-1)*(len_s%block_len):]
		blocks = [s[idx*block_len:idx*block_len+block_len] for idx in range(len_s//block_len)]
		zipped, block, count = "", "", 0
		while blocks:
			block, blocks = blocks[0], blocks[1:]
			blocks, count = zipper(blocks, block)
			if count == 1:
				zipped += f"{block}"
			else:
				zipped += f"{count}{block}"
		zipped += whats_left

		if len(zipped) < answer:
			answer = len(zipped)
	
	return answer