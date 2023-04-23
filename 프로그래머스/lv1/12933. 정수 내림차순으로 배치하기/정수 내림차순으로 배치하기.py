def solution(n):
    answer = 0
    str_n = str(n)
    test_list=[]
    for i in str_n:
        test_list.append(int(i))
    test_list.sort(reverse=True)
    for i in range(len(str_n)):
        answer+=test_list[i]*(10**(len(str_n)-i-1))
    return answer