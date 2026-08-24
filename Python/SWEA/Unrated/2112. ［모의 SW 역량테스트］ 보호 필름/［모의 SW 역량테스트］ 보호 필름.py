def test(arr, K):
    if K <= 1:
        return True

    for c in range(W):
        count = 1
        for r in range(1, D):
            if arr[r][c] == arr[r - 1][c]:
                count += 1
                if count >= K:
                    break
            else:
                count = 1
        if count < K:
            return False
    return True


# 행단위로 DFS(행, 약품투입횟수)
def dfs(row, inserted):
    global answer

    # K번 이상 투입하면 무조건 통과
    if inserted >= answer:
        return

    if test(arr, K):
        answer = inserted
        return

    if row == D:
        return

    # 원본 백업
    row_bak = arr[row]
    # 1. 그대로
    dfs(row + 1, inserted)

    # 2. 이 행에 A 주입
    arr[row] = [0] * W
    dfs(row + 1, inserted + 1)

    # 3. 이 행에 B 주입
    arr[row] = [1] * W
    dfs(row + 1, inserted + 1)
    # 백트래킹
    arr[row] = row_bak


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    D, W, K = map(int, input().split())
    arr = []
    # D: 보호필름 두께, W: 보호필름 가로크기, K: 합격기준
    for _ in range(D):
        arr.append(list(map(int, input().split())))

    answer = K
    dfs(0, 0)
    print(f"#{test_case} {answer}")
