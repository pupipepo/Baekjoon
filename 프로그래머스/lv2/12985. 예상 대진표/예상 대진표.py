def solution(n,a,b):
    answer = 0
    max_n=len(bin(n)[2:])
    answer = max_n
    bin_a=bin(a-1)[2:].zfill(max_n)
    bin_b=bin(b-1)[2:].zfill(max_n)
    for i in range(max_n):
        if bin_a[i] != bin_b[i]:
            break
        else:
            answer-=1

    return answer