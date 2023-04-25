def solution(d, budget):
    answer = 0
    test = 0
    d.sort()
    for i in d:
        test += i
        if test<=budget:
            answer+=1
        else:
            break
    return answer