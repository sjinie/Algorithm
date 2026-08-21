directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 상하좌우
blocks = [(0, 1, 2, 3), (1, 3, 0, 2), (3, 0, 1, 2), (2, 0, 3, 1), (1, 2, 3, 0), (1, 0, 3, 2)]
# 0 = 빈칸, 1~5 블록, 6~10 웜홀, -1 블랙홀


def simulate(arr, wormhole, sr, sc, d):
    score = 0
    direction = d
    r, c = sr, sc

    while True:
        dr, dc = directions[direction]
        nr = r + dr
        nc = c + dc

        # boundary (점수 +1)
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            direction = blocks[5][direction]
            score += 1
        else:
            # 다음칸 이동
            r, c = nr, nc

        num = arr[r][c]

        # 출발 위치로 돌아왔을때
        if (r, c) == (sr, sc):
            break
        # 다음 칸이 블랙홀일때
        elif num == -1:
            break

        # 다음 칸이 블록일때 (점수 +1)
        elif 1 <= num <= 5:
            direction = blocks[num][direction]
            score += 1

        # 다음 칸이 웜홀일때
        elif 6 <= num <= 10:
            a, b = wormhole[num]
            if (r, c) == a:
                r, c = b
            else:
                r, c = a
    return score


def get_max(arr, wormhole):
    max_score = 0

    for r in range(N):
        for c in range(N):
            if arr[r][c] != 0:
                continue
            # 빈칸에서만 출발 가능
            for d in range(4):
                max_score = max(max_score, simulate(arr, wormhole, r, c, d))

    return max_score


# 최대 점수 찾기

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    wormhole = [[] for _ in range(11)]

    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(N):
            if 6 <= row[c] <= 10:
                wormhole[row[c]].append((r, c))
                # 웜홀 좌표 저장
        arr.append(row)
        # 입력

    answer = get_max(arr, wormhole)
    print(f"#{test_case} {answer}")