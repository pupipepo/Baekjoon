def solution(n, m):
    multi = n*m
    answer = []
    while n !=0:
        t = m%n
        (m,n) = (n,t)
    answer.append(abs(m))
    answer.append(multi/abs(m))

    return answer