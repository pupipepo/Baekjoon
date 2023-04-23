def solution(arr):
    min_num = min(arr)
    min_index=arr.index(min_num)
    arr.pop(min_index)
    answer=arr
    if len(answer)==0:
        answer=[-1]
    return answer