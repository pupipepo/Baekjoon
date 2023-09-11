import sys
M = int(sys.stdin.readline().rstrip())
S = []
for i in range(M):
  command = sys.stdin.readline().rstrip().split(' ')
  if command[0] == 'empty':
    S = []
  elif command[0] == 'all':
    S = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
  elif command[0] == 'add':
    if int(command[1]) not in S:
      S.append(int(command[1]))
  elif command[0] == 'remove':
    if int(command[1]) in S:
      S.remove(int(command[1]))
  elif command[0] == 'check':
    if int(command[1]) in S:
      print(1)
    else:
      print(0)
  elif command[0] == 'toggle':
    if int(command[1]) in S:
      S.remove(int(command[1]))
    else:
      S.append(int(command[1]))