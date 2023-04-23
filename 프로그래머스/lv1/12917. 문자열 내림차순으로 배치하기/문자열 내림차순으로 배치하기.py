def solution(s):
    answer=''
    test = sorted(s, reverse=True)
    for i in test:
        answer+=i
    return answer