def solve(arr, m):
    max_kill = 0
    for r in range(n-m+1):
        for c in range(n-m+1):
            max_kill = max(max_kill, sum([sum(row[c:c+m]) for row in arr[r:r+m]]))
    return max_kill

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    answer = solve(arr, m)
    print(f'#{test_case} {answer}')