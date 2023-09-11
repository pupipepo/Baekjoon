import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums.sort()
ans=0
for i in range(N):
  ans+=nums[i]*(len(nums)-i)
print(ans)