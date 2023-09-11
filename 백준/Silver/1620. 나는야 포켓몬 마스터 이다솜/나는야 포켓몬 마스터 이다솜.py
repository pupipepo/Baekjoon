import sys

N, M = sys.stdin.readline().rstrip().split()
N = int(N); M = int(M)
names={}
for i in range(1,N+1):
  names[i] = sys.stdin.readline().rstrip()
nums = {v:k for k,v in names.items()}
for i in range(M):
  command = sys.stdin.readline().rstrip()
  if command.isdigit():
    print(names.get(int(command)))
  else:
    print(nums.get(command))