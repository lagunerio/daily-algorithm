def solution(s):
    answer = []
    round, removed = 0, 0
    
    while s != "1":
        round += 1
        # 1
        length = len(s)
        s = str(s).replace("0","")
        removed += (length - len(s))
        # 2
        c = len(s)
        tmp = []
        while c>1:
            tmp.append(str(c%2))
            c = c//2
        tmp.append(str(c))
        s = ""
        while tmp:
            s += tmp.pop()
        
    
    return [round, removed]
