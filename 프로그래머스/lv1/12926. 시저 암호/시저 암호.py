from string import ascii_lowercase
from string import ascii_uppercase

def solution(s, n):
    answer = ''
    Lower=ascii_lowercase
    Upper=ascii_uppercase
    for i in s:
        if i==' ':
            answer+=' '
        elif i in Lower:
            idx=Lower.index(i)
            answer+=Lower[(idx+n)%26]
        else:
            idx=Upper.index(i)
            answer+=Upper[(idx+n)%26]
    return answer