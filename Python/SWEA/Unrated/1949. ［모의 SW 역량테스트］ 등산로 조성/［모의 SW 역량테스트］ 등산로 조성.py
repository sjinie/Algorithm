directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_peak(arr, N):
    # 봉우리 좌표 찾기
    max_height = max(map(max, arr))
    peaks = [(r, c) for r in range(N) for c in range(N) if arr[r][c] == max_height]
    return peaks


def dfs(r, c, k_used, route_length, arr, visited, n, K):
    max_length = route_length
    visited[r][c] = True
	# 상하좌우 이동
    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc]:
            continue
        # 이동불가

        if arr[nr][nc] < arr[r][c]:  # 높이가 낮을때
            max_length = max(max_length, dfs(nr, nc, k_used, route_length + 1, arr, visited, n, K))
        elif (not k_used) and (arr[nr][nc] - K < arr[r][c]):
            original_height = arr[nr][nc]
            arr[nr][nc] = arr[r][c] - 1
            # 이동하려는 칸의 높이를 최대 K만큼 깎아서 현재 위치보다 낮게 만들 수 있다면, 현재 위치보다 1 낮게 만들고 이동
            max_length = max(max_length, dfs(nr, nc, True, route_length + 1, arr, visited, n, K))
            arr[nr][nc] = original_height
            # 이동하고 높이 복구 (백트래킹)
    visited[r][c] = False
    # 방문여부 초기화 (백트래킹)
    return max_length


def explore(peaks, arr, K):
    # 모든 봉우리에서 탐색 시작
    n = len(arr)
    visited = [[False] * n for _ in range(n)]
    max_length = 0

    for sr, sc in peaks:
        max_length = max(max_length, dfs(sr, sc, False, 1, arr, visited, n, K))

    return max_length


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    peaks = find_peak(arr, N)
    answer = explore(peaks, arr, K)

    print(f"#{test_case} {answer}")