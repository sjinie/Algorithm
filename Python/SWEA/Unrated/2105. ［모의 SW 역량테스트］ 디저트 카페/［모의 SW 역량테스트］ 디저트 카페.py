directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def explore(r, c, a, b):
    # 해당 경로에 중복되는 숫자(디저트)가 있는지 검사
    diagonal_length = [a, b, a, b]
    dessert = []
    sr, sc = r, c

    for d in range(4):
        dr, dc = directions[d]
        for _ in range(diagonal_length[d]):
            # 검사
            if cafe[sr][sc] in dessert:
                return -1
            dessert.append(cafe[sr][sc])
            sr, sc = sr + dr, sc + dc
    return len(dessert)


# 해당 위치에서 대각선 성분 결정
#     (r,c)에서 시작
# 0<=c-b           c+a<N
#         r+a+b<N
def diagonal(r, c):
    max_visited = -1
    # for a,b loop 돌면서 가능한 a,b 조합에서 explore
    for a in range(1, N - c):
        b_range = min(c + 1, N - a - r)
        for b in range(1, b_range):
            # 대각선 성분마다 탐색
            visited = explore(r, c, a, b)

            # 해당 위치에서 방문할 수 있는 카페가 0보다 크다면 최댓값 갱신
            if visited > 0:
                max_visited = max(visited, max_visited)

    return max_visited


# 탐색이 가능한 시작 위치 결정
def simulate():
    answer = -1
    for r in range(N - 2):
        for c in range(1, N - 1):
            answer = max(answer, diagonal(r, c))
    return answer


# 입력 처리
def get_input():
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    return arr, N


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cafe, N = get_input()
    answer = simulate()
    print(f"#{test_case} {answer}")
