from collections import deque


def calculate_time(arrivals, stair_length):
    arrivals.sort()

    queue = deque()
    last_finish = 0

    for arrival in arrivals:
        # 계단에 들어갈 수 있는 시간
        enter_time = arrival + 1

        # 계단에 이미 3명이 있으면
        if len(queue) == 3:
            first_finish = queue.popleft()
            enter_time = max(enter_time, first_finish)
        # 계단에 먼저 들어간 1명이 빠지고 나서 들어갈 수 있음
        finish_time = enter_time + stair_length
        queue.append(finish_time)

        last_finish = finish_time

    return last_finish


def move_to_stairs(people, stairs, selected):
    # manhattan distance 계산
    stair0 = []
    stair1 = []
    for i in range(len(selected)):
        # selected : i번째 사람이 어느 계단으로 갔는지
        pr, pc = people[i]
        if selected[i] == 0:
            sr, sc, _ = stairs[0]
            distance = abs(pr - sr) + abs(pc - sc)
            stair0.append(distance)
        if selected[i] == 1:
            sr, sc, _ = stairs[1]
            distance = abs(pr - sr) + abs(pc - sc)
            stair1.append(distance)
    stair0_finish_time = calculate_time(stair0, stairs[0][2])
    stair1_finish_time = calculate_time(stair1, stairs[1][2])

    return max(stair0_finish_time, stair1_finish_time)
    # 계단0, 계단1 전부 내려가야 완료


def dfs(idx, people, stairs, selected):
    if idx == len(people):
        # 계단에 사람 다 배정했으면 시간 계산
        time = move_to_stairs(people, stairs, selected)
        return time

    # 현재 idx의 사람을 0번째 계단에 배치했을때
    selected.append(0)
    time0 = dfs(idx + 1, people, stairs, selected)
    selected.pop()

    # 현재 idx의 사람을 1번째 계단에 배치했을때
    selected.append(1)
    time1 = dfs(idx + 1, people, stairs, selected)
    selected.pop()

    return min(time0, time1)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    people = []
    stairs = []
    selected = []
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(N):
            if row[c] == 1:
                people.append((r, c))
            elif row[c] > 1:
                stairs.append((r, c, row[c]))
    answer = dfs(0, people, stairs, selected)
    print(f"#{test_case} {answer}")