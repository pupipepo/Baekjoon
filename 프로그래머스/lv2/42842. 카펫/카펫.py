def solution(brown, yellow):
    # brown = 가로+가로+세로-2+세로-2
    # yellow = (가로-2)*(세로-2)
    # brown+yellow = 가로*세로
    tiles=brown+yellow
    answer = []
    for i in range(3, int(tiles**0.5)+1):
        if tiles%i ==0:
            garo = tiles//i
            sero = i
            if garo + sero -2 == brown//2:
                answer.append(garo)
                answer.append(sero)
            
    
    return answer