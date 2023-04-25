def solution(n):
    answer = 0
    bin_n = bin(n)[2:]
    n_count = bin_n.count('1')
    while True:
        n+=1
        bin_n = bin(n)[2:]
        new_n_count = bin_n.count('1')
        if n_count==new_n_count:
            answer=n
            break
    return answer