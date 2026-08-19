# 행 하나 받아서 dfs로 탐색하면서 최대 점수 계산

def dfs(arr, sum):
    global max_score

    if len(arr) == 1:
        max_score = max(max_score, sum + arr[0])
        return

    for idx in range(len(arr)):
        # 점수계산
        if idx == 0:
            score = arr[1]
        elif idx == len(arr) - 1:
            score = arr[-2]
        else:
            score = arr[idx - 1] * arr[idx + 1]

        # idx 블록 제거
        removed = arr.pop(idx)
        dfs(arr, sum + score)
        # 백트래킹
        arr.insert(idx, removed)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 입력
    max_score = 0

    dfs(arr, 0)
    print(f"#{test_case} {max_score}")
