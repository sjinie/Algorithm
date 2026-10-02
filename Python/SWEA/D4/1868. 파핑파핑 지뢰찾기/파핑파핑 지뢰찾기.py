#import sys
from collections import deque

#sys.stdin = open("input.txt", "r")

"""
이 숫자가 0이라면 근처의 8방향에 지뢰가 없다는 것이 확정된 것이기 때문에 그 8방향의 칸도 자동으로 숫자를 표시해 준다.
--> 근처 8방향에 지뢰가 없는, 숫자가 0인 칸만 주변이 밝혀지는 것임
--> 0인 칸을 클릭하면 9칸이 밝혀지고, 나머지는 한칸씩 밝혀야함 (visit)
"""


dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # 8방향 회전

def check(r, c):
    num = 0
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if not (0<=nr<N and 0<=nc<N):
            continue
        if grid[nr][nc] == '*':
            num += 1
    grid[r][c] = num

def bfs(sr, sc, visited):
    visited[sr][sc] = True
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc]:
                continue
            visited[nr][nc] = True # 큐에 넣을때 방문처리
            if grid[nr][nc] == 0:           
                q.append((nr, nc))


def explore(grid): # 먼저 grid 돌면서 숫자 채우기
    click = 0
    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if grid[r][c] != '*':
                check(r,c)

    # 주변 8칸에 지뢰가 없는 0부터 bfs로 방문처리 후 클릭
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 0 and not visited[r][c]:
                bfs(r,c, visited)
                click += 1
	# 나머지 칸들은 하나씩 클릭
    for r in range(N):
        for c in range(N):
            if grid[r][c] != '*' and not visited[r][c]:
                visited[r][c] = True
                click += 1
    return click

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    N = int(input())
    grid = [list(input().strip()) for _ in range(N)]
    answer = explore(grid)
    print(f'#{test_case} {answer}')