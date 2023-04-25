def solution(array, commands):
    answer=[]
    for i in range(len(commands)):
        a= commands[i][0]
        b= commands[i][1]
        c= commands[i][2]
        new_list=array[a-1:b]
        new_list.sort()
        answer.append(new_list[c-1])
    return answer