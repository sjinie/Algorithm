T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다. 
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    
    dp = [0]*(L+1)
    for i in range(N):
        score = arr[i][0]
        kcal = arr[i][1]
        for c in range(L, kcal-1, -1):
            dp[c] = max (
                dp[c],
                dp[c-kcal]+score
            )
    print(f"#{test_case} {dp[L]}")