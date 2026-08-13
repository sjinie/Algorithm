# N*N arr에서 가로로 연속된 M개의 꿀통 선택 (일꾼 2명은 서로 겹치지 않아야함)
# 이 중에서 꿀통의 숫자합이 C 이하가 되도록 subset 선택
# 선택한 subset 제곱합 max 구하기

# 행 하나를 받아서 시작부터 DFS로 탐색하면서, 합이 C 이하인 subset의 제곱합의 최댓값을 return
def subset(row, C):
    max_squared_sum = 0
    def dfs(idx, sum, squared_sum):
        nonlocal max_squared_sum
        if sum > C:  # 합이 C를 넘으면 더 이상 진행하지 않음
            return
        if idx == len(row):  # M개를 다 골랐으면 제곱합 갱신
            max_squared_sum = max(max_squared_sum, squared_sum)
            return
        # 선택하는 경우
        dfs(idx + 1, sum + row[idx], squared_sum + row[idx] ** 2)
        # 선택하지 않는 경우
        dfs(idx + 1, sum, squared_sum)

    dfs(0, 0, 0)
    return max_squared_sum    


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, C = map(int,input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    # 입력

    max_profit = 0
    ssr_arr = []

    for r in range(N):
        for c in range(N-M+1):
            ssr_arr.append(subset(arr[r][c:c+M],C))

    # ssr_arr에는 각 위치에서 시작해서 M개의 꿀통 선택시 나온 조건부 최대 제곱합이 들어있음
    # column이 다르거나, 아니면 column이 같더라도 row가 달라야 안겹침
    for r1 in range(N):
        for c1 in range(N-M+1):
            for r2 in range(N):
                for c2 in range(N-M+1):
                    if r1 == r2 and (c1 + M > c2 and c2 + M > c1):  # 겹치는 경우
                        continue
                    max_profit = max(max_profit, ssr_arr[r1*(N-M+1)+c1] + ssr_arr[r2*(N-M+1)+c2])

    print(f'#{test_case} {max_profit}')