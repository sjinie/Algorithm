def simulate(n, m, grid):
    pw = [0] * (n + 1) 
    pb = [0] * (n + 1)
    pr = [0] * (n + 1)
	# 초기화
    
    for r in range(n):
        row = grid[r]
        pw[r + 1] = pw[r] + m - row.count("W") # 0~r까지 하양으로 바꾸는 횟수
        pb[r + 1] = pb[r] + m - row.count("B") # 0~r까지 파랑으로 바꾸는 횟수
        pr[r + 1] = pr[r] + m - row.count("R") # 0~r까지 빨강으로 바꾸는 횟수
		# row마다 색칠횟수 누적합
    minimum = n * m
    
    for w in range(1, n - 1): # 맨 위 흰색
        for b in range(w + 1, n): # w-b행만큼 파란색, n-b만큼 빨간색
            cnt = pw[w] + (pb[b] - pb[w]) + (pr[n] - pr[b])
            minimum = min(minimum, cnt)
    return minimum

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N , M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]
    answer = simulate(N, M, grid)
    print(f"#{test_case} {answer}")