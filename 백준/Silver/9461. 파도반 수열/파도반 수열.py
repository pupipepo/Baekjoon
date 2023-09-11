import sys

N = int(sys.stdin.readline().rstrip())
d=[1]*101
for i in range(4,101):
  d[i] = d[i-2]+d[i-3]
for j in range(N):
  num = int(input())
  print(d[num])