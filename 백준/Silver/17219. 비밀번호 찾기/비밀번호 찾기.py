import sys

N, M = sys.stdin.readline().rstrip().split()
N = int(N); M = int(M)
passwords={}
for _ in range(N):
  k, v = sys.stdin.readline().rstrip().split()
  passwords[k]=v
for _ in range(M):
  print(passwords[sys.stdin.readline().rstrip()])