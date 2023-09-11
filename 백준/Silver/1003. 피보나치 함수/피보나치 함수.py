import sys

N = int(sys.stdin.readline().rstrip())
list_0 = [0] * 41
list_1 = [0] * 41

list_0[0]=1
list_1[1]=1

for i in range(2,41):
  list_0[i] = list_0[i-1] + list_0[i-2]
  list_1[i] = list_1[i-1] + list_1[i-2]

for _ in range(N):
  num = int(sys.stdin.readline().rstrip())
  print(f'{list_0[num]} {list_1[num]}')