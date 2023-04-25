def solution(s):
    answer = ''
    cursor=0
    for i in s:
        if i==' ':
            answer+=' '
            cursor = 0
        else:
            cursor +=1
            if cursor ==1:
                answer+=i.upper()
            else:
                answer+=i.lower()
    return answer