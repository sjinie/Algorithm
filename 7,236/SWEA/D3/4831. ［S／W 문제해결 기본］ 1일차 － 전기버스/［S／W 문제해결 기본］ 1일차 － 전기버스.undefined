def interval(start, answer):
    if start + K >= N:
        return answer
    for i in range(start + K, start, -1):
        if i in stops:
            return interval(i, answer + 1)
    return 0

T = int(input())
for test_case in range(1, T + 1): 
    K, N, M = map(int, input().split())
    stops = list(map(int, input().split()))
    print(f"#{test_case} {interval(0, 0)}")