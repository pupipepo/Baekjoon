import sys

N, M = sys.stdin.readline().rstrip().split()
N = int(N); M = int(M)
no_deut =[]
ans =[]
for i in range(N):
  no_deut.append(sys.stdin.readline().rstrip())
no_deut=set(no_deut)
for i in range(M):
  no_bo = (sys.stdin.readline().rstrip())
  if no_bo in no_deut:
    ans.append(no_bo)
print(len(ans))
ans.sort()
for i in ans:
  print(i)