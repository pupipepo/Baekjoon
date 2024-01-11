import sys
input = sys.stdin.readline
from collections import deque

move_x = [1,-1,0,0]
move_y = [0,0,1,-1]

n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)]

def bfs(i, j, color):
    queue = deque()
    queue.append((i,j)) # 지금 커서(? 확인하고 있는 곳) 의 위치
    graph[i][j] = 'v' # 확인한 곳을 v 로 표시
    count = 1 # 해당 위치에 있는 녀석 1명으로 출발

    while queue: # 인접했으면서 같은 색인데 visited 하지 않은 녀석이 없을 때까지 반복
        x, y = queue.popleft()
        for i in range(4):
            new_x, new_y = x+move_x[i], y+move_y[i]
            if 0 <= new_x < m and 0 <= new_y < n: # graph 범위 안에 있으면
                if graph[new_x][new_y] != 'v' and graph[new_x][new_y]==color:
                    graph[new_x][new_y]= 'v'
                    queue.append((new_x,new_y)) # 같은 색이니까 탐색할 대상에 추가
                    count += 1 # new_x, new_y에 있는 녀석 추가
    return count # 뭉쳐 있는 녀석의 숫자 반환

W_strength, B_strength = 0, 0

for i in range(m):
    for j in range(n):
        if graph[i][j] != 'v':
            if graph[i][j] == 'W':
                W_strength += bfs(i,j,graph[i][j])**2
            else:
                B_strength += bfs(i,j,graph[i][j])**2

print(W_strength, B_strength)