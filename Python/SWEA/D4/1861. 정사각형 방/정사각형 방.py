T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다. 
dir= [[1,0],[-1,0],[0,1],[0,-1]]

def dfs(i,j):
    # dp[i][j] = (i,j)에 도달했을때 몇개의 방을 이동할 수 있는지
    if (dp[i][j] != 0):
        return dp[i][j]
    dp[i][j] = 1
    # DFS 한적 없으면 일단 자기 자신 방문
    for dr,dc in dir:
        next_i = i + dr
        next_j = j + dc   
        if (0 <= next_i < N) and (0 <= next_j < N):
            if(arr[next_i][next_j] == arr[i][j]+1):
                # DFS로 탐색하면서 이동횟수+1
                dp[i][j] = max(dp[i][j], 1 + dfs(next_i, next_j))
    return dp[i][j]
#DFS

for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    # 입력
    dp = [[0]*N for _ in range(N)] 
    max_count = 0
    start = 0
    # 초기화
    for i in range(N):
        for j in range(N):
            count = dfs(i,j)
            if(max_count < count):
                max_count = count
                start = arr[i][j]
            elif(max_count == count):
                start = min(arr[i][j], start)
    print(f"#{test_case} {start} {max_count}")