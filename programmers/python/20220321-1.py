# 프로그래머스 - 코딩테스트 연습 > 위클리 챌린지 > 피로도
from itertools import permutations

def round(k, dungeons_inorder):
    idx = 0
    while len(dungeons_inorder) > idx:
        if dungeons_inorder[idx][0] <= k:
            k -= dungeons_inorder[idx][1]
            idx += 1
        else:
            return idx
    return idx

def solution(k, dungeons):
    answer = 0
    for order in permutations(dungeons, len(dungeons)):
        round_cnt = round(k, list(order))
        if round_cnt > answer:
            answer = round_cnt
    
    return answer
