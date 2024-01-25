import sys
input = sys.stdin.readline

n = int(input())

scores=[]
for i in range(n):
    name, kor, eng, math = input().split()
    scores.append((name, int(kor), int(eng), int(math)))

scores.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))
for score in scores:
    print(score[0])