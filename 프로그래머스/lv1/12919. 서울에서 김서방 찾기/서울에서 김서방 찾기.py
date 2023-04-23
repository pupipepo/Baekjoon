def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i]=="Kim":
            idx=i
    return "김서방은 {}에 있다".format(idx)