def solution(n):
    answer = []
    str_n = str(n)
    for i in range(len(str_n)):
        answer.append(int(str_n[len(str_n)-i-1]))
    return answer