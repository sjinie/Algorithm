# 손해를 보지 않으면서 홈방법 서비스를 가장 많이 제공받는 경우
def solve(city, houses):
    max_serviced = 0
    N = len(city)
    for sr in range(N):
        for sc in range(N):
            # 0,0이 중심일때 (n-1,n-1)이 마름모꼴에 포함되려면 manhattan distance = 2(n-1)이 k의 최댓값
            for k in range(1, 2 * (N - 1)):
                serviced = 0
                cost = k * k + (k - 1) * (k - 1)
                for r, c in houses:
                    # 마름모꼴 안에 있다 -> 중심으로부터의 manhattan distance가 k보다 작다
                    distance = abs(sr - r) + abs(sc - c)
                    if distance < k:
                        serviced += 1
                profit = serviced * M - cost
                # profit이 0보다 큰 경우에만 서비스 받는 집의 개수 최댓값 갱신
                if profit >= 0:
                    max_serviced = max(max_serviced, serviced)
    return max_serviced


# 입력 처리
def get_input():
    N, M = map(int, input().split())
    arr = []
    houses = []
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(N):
            if row[c] != 0:
                houses.append((r, c))
        arr.append(row)
    return arr, houses, M


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    city, houses, M = get_input()
    answer = solve(city, houses)

    print(f"#{test_case} {answer}")
