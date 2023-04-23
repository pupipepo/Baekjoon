def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        ans_list=[]
        for j in range(len(arr1[i])):
            ans_list.append(arr1[i][j]+arr2[i][j])
        answer.append(ans_list)
    return answer