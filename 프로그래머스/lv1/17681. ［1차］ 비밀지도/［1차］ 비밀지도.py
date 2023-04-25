def solution(n, arr1, arr2):
    answer = []
    for i in range(n): #row 갯수만큼 iteration 합니다.
        row_str=''
        map1= bin(arr1[i])[2:].zfill(n)
        map2= bin(arr2[i])[2:].zfill(n)
        for j in range(n):
            if map1[j]=='0' and map2[j]=='0':
                row_str+=' '
            else:
                row_str+='#'
        answer.append(row_str)
    return answer