def solution(n):
    answer = 1
    for i in range(1,n):
        test=0
        for j in range(i,n):
            test+=j
            if test==n:
                answer+=1
                break
            elif test>n:
                break
    return answer