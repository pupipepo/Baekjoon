def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        num_list=[]
        for j in range(1,i+1):
            if i%j==0:
                num_list.append(j)
        if len(num_list)%2==0:
            answer +=i
        else:
            answer -=i
    return answer