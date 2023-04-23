def solution(x):
    answer = False
    str_x = str(x)
    devision_num = 0
    for i in str_x:
        devision_num+=int(i)
    if x%devision_num==0:
        answer = True
    return answer