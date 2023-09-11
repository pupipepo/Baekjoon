import sys

N, M = sys.stdin.readline().rstrip().split()
N = int(N); M = int(M)
num_coins=0
coins=[]
for i in range(N):
  coins.append(int(sys.stdin.readline().rstrip()))
while M>0:
  biggest_coin = coins.pop()
  count = M//biggest_coin
  num_coins += count
  M -= count*biggest_coin
print(num_coins)