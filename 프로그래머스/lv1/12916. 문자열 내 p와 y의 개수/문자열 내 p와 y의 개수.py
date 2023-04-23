def solution(s):
    answer = False
    s=s.lower()
    p_num=s.count('p')
    y_num=s.count('y')
    if p_num==y_num:
        answer=True
    return answer