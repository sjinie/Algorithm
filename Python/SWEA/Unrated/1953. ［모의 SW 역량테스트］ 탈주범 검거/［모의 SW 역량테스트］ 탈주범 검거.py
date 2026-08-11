from collections import deque

type = [
    (0, 0, 0, 0),
    (1, 1, 1, 1),
    (1, 1, 0, 0),
    (0, 0, 1, 1),
    (1, 0, 0, 1),
    (0, 1, 0, 1),
    (0, 1, 1, 0),
    (1, 0, 1, 0),
]
reverse = [1, 0, 3, 2]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 상하좌우

def bfs(r, c, tunnel, dir, L):
    n = len(tunnel)
    m = len(tunnel[0])
    visited = [[False] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]

    q = deque([(r, c)])
    visited[r][c] = True
    count = 1
    # 자기 자신 방문 처리

    while q:
        r, c = q.popleft()
        for i in range(4):
            # 현재위치에서 상하좌우로 이동
            if type[tunnel[r][c]][i] == 1:
                # 현재위치에서 이동가능한 방향인지
                nr = r + dir[i][0]
                nc = c + dir[i][1]
                # 이동하려는 위치에 터널이 있으면
                if (
                    0 <= nr < n
                    and 0 <= nc < m
                    and not visited[nr][nc]
                    and tunnel[nr][nc] != 0
                ):
                    # 이동가능한 위치인지 확인
                    if type[tunnel[nr][nc]][reverse[i]] == 1:
                        # 이동하려는 위치에서 반대방향으로 길 뚫려있는지
                        visited[nr][nc] = True
                        dist[nr][nc] = dist[r][c] + 1
                        if dist[nr][nc] < L:
                            count += 1
                            q.append((nr, nc))
    return count

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = []
    for _ in range(N):
        tunnel.append(list(map(int, input().split())))
    # 입력
    count = bfs(R, C, tunnel, dir, L)
    print(f"#{test_case} {count}")