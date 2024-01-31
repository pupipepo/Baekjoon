import sys
input = sys.stdin.readline

n = int(input())
tree_init = list(map(int, input().split()))
tree_growth = list(map(int, input().split()))
trees = sorted(zip(tree_init, tree_growth), key=lambda x:x[1])
ans = 0
for i in range(n):
    ans += trees[i][0]+trees[i][1]*i
print(ans)