def solution(n, words):
    answer = []
    L=[]
    for i in range(len(words)):
        if len(L)==0:
            L.append(words[i])
        elif words[i] in L:
            member = (i+1)%n
            times = ((i+1)//n)+1
            if member ==0:
                member=n
                times -=1
            answer.append(member)
            answer.append(times)
            break
        elif L[-1][-1] != words[i][0]:
            member = (i+1)%n
            times = ((i+1)//n)+1
            if member ==0:
                member=n
                times -=1
            answer.append(member)
            answer.append(times)
            break
        else:
            L.append(words[i])
    if L==words:
        answer=[0,0]
    return answer