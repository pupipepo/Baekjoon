def solution(n):
    answer = -1
    if abs(n**0.5 - int(n**0.5))<=0.01:
        answer = ((n**0.5)+1)**2
    return answer