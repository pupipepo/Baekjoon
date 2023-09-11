import sys

N = int(sys.stdin.readline().rstrip())
for i in range(N):
  M = int(sys.stdin.readline().rstrip())
  types={}
  for j in range(M):
    name, type = sys.stdin.readline().rstrip().split()
    if type in types:
      types[type] += 1
    else:
      types[type] = 2
  ans =1
  for k in types.values():
    ans*=k
  print(ans-1)
    