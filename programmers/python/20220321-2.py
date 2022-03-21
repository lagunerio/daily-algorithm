# 프로그래머스 - 코딩테스트 연습 > 위클리 챌린지 > 전력망을 둘로 나누기
def dfs(wire_dict, root):
	visit, stack = [], []
	stack.append(root)
	while stack:
		node = stack.pop()
		if node not in visit:
			visit.append(node)
			stack.extend(wire_dict[node])

	return visit

def get_nodes_diff(wires, idx):
	from collections import defaultdict
	wire_dict = defaultdict(list)
	for wire in (wires[:idx] + wires[idx+1:]):
		wire_dict[wire[0]].append(wire[1])
		wire_dict[wire[1]].append(wire[0])

	left_nodes = len(dfs(wire_dict, wires[idx][0]))
	right_nodes = len(dfs(wire_dict, wires[idx][1]))

	if left_nodes > right_nodes:
		return left_nodes - right_nodes
	else:
		return right_nodes - left_nodes


def solution(n, wires):
	answer = len(wires)
	wires.sort(key = lambda x: x)
	
	for idx, wire in enumerate(wires):
		tmp = get_nodes_diff(wires, idx)
		if tmp < answer:
			answer = tmp

	return answer