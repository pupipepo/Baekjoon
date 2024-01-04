import sys
input = sys.stdin.readline
# 이 집을 빨강, 초록, 파랑으로 칠했을 때의 최소 비용을 각각 계속 구해주면 된다.

n = int(input())
cost = list(map(int, input().split(' ')))
for i in range(1, n):
    cost_r_old, cost_g_old, cost_b_old = cost[0], cost[1], cost[2]
    cost_r_now, cost_g_now, cost_b_now = map(int, input().split(' '))
    cost_r_new = min(cost_g_old+cost_r_now, cost_b_old+cost_r_now)
    cost_g_new = min(cost_r_old+cost_g_now, cost_b_old+cost_g_now)
    cost_b_new = min(cost_r_old+cost_b_now, cost_g_old+cost_b_now)
    cost = [cost_r_new, cost_g_new, cost_b_new]
print(min(cost))