def solution(s):
    answer = False
    if len(s)==4 or len(s)==6:
        try:
            for i in range(len(s)):
                int(s[i])
            answer=True
        except:
            answer=False
    return answer