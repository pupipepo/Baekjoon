def solution(num):
    i=0
    while i<500:
        if num%2==0:
            num/=2
            i+=1
            if num==1:
                break
        elif num==1:
            i=0
            break
        else:
            num*=3
            num+=1
            i+=1
    if i == 500:
        i=-1
    return i