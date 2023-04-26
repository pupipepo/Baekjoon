def solution(people, limit):
    answer = 0
    people.sort()
    big=len(people)-1
    small=0
    while True:
        boat=people.pop()
        big -=1
        if boat+people[small]<=limit:
            small+=1
        answer+=1
        if small >big:
            break
        elif small==big:
            answer+=1
            break
    return answer