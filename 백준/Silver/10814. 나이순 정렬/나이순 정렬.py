N = int(input())
ans_list=[]
for _ in range(N):
  age, name = input().split()
  ans_list.append([age, name])
ans_list.sort(key=lambda x: int(x[0]))
for val in ans_list:
  print(*val)