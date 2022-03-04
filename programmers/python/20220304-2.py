import math

def solution(n):
    answer = 0
    
    base_three = []
    while n>2:
        base_three.append(n%3)
        n = n//3
    base_three.append(n)
    
    for loc, num in enumerate(base_three):
        answer += num*pow(3,len(base_three) - loc - 1)
    
    return answer
