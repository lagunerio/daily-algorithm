# 프로그래머스 - 코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT > 오픈채팅방
from collections import defaultdict

def solution(records):
	answer = []
	users = defaultdict()
	log = []

	for record in records:
		record_type = record.split(" ")[0]

		if record_type == "Leave":
			uid = record.split(" ")[1]
			log.append([uid, record_type])
		elif record_type == "Enter":
			uid, nickname = record.split(" ")[1:]
			users[uid] = nickname
			log.append([uid, record_type])
		elif record_type == "Change":
			uid, nickname = record.split(" ")[1:]
			users[uid] = nickname

	message = {
		"Enter": "님이 들어왔습니다.",
		"Leave": "님이 나갔습니다."
	}

	for raw in log:
		answer.append(f"{users[raw[0]]}{message[raw[1]]}")

	return answer
