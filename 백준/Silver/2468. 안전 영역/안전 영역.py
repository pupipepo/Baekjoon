import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = []
visited =[]
move_x = [1,-1,0,0]; move_y = [0,0,1,-1]
for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(i, j, rain):
    queue = deque()
    is_ok=0
    if visited[i][j] != True and graph[i][j] > rain:
        queue.append((i,j)) # 지금 커서(? 확인하고 있는 곳) 의 위치
        is_ok=1
    visited[i][j] = True # 확인한 곳을 v 로 표시

    while queue: # 인접했으면서 같은 색인데 visited 하지 않은 녀석이 없을 때까지 반복
        x, y = queue.popleft()
        for i in range(4):
            new_x, new_y = x+move_x[i], y+move_y[i]
            if 0 <= new_x < n and 0 <= new_y < n: # graph 범위 안에 있으면
                if visited[new_x][new_y] != True and graph[new_x][new_y] > rain:
                    visited[new_x][new_y]= True
                    queue.append((new_x,new_y)) # 안전한 곳이니까 탐색 대상에 추가
                    
    return is_ok # 덩어리 하나 반환

safe_land=[]
for rain in range(max(map(max,graph))):
    visited = [[False]*n for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            ans += bfs(i,j,rain)
    safe_land.append(ans)

print(max(safe_land))