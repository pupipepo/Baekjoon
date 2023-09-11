import sys

N, M = sys.stdin.readline().rstrip().split()
N=int(N); M=int(M)
nums = list(map(int, sys.stdin.readline().rstrip().split()))
cum_sum=[nums[0]]

for k in range(1,N):
  cum_sum.append(cum_sum[k-1]+nums[k])
for i in range(M):
  start, end = sys.stdin.readline().rstrip().split()
  start = int(start)-2
  end = int(end)-1
  if start <0:
    print(cum_sum[end])
  else:
    print(cum_sum[end]-cum_sum[start])