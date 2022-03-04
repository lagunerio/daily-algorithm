def solution(numbers):
    answer = []
    for idx in range(0, len(numbers)-1):
        for jdx in range(idx+1, len(numbers)):
            answer.append(numbers[idx] + numbers[jdx])
    answer = list(set(answer))
    answer.sort()
    return answer
