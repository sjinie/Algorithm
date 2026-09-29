def get_score(magnets):
    # 각 자석의 12시 방향 자성으로 최종 점수를 계산
    return sum(magnets[idx][0] * (2 ** idx) for idx in range(4))


def check_polarity(magnets, left, right):
    # 인접한 두 자석의 접촉면이 다르면 True를 반환한다.
    return magnets[left][2] != magnets[right][6]


def turn_left(magnets, idx):
    # 자석 하나를 반시계방향으로 한 칸 회전시킨다.
    magnet = magnets[idx]
    magnet.append(magnet.pop(0)) # 0번째를 pop해서 제일 마지막에 넣음


def turn_right(magnets, idx):
    # 자석 하나를 시계방향으로 한 칸 회전시킨다.
    magnet = magnets[idx]
    magnet.insert(0, magnet.pop()) # 마지막을 빼서 0번째에 넣음


def get_rotations(magnets, main, direction):
    # main 자석 기준으로 각 자석의 회전 방향을 계산
    rotations = [0] * 4
    rotations[main] = direction

    # main부터 왼쪽으로 전파
    for idx in range(main, 0, -1):
        if not check_polarity(magnets, idx - 1, idx):
            break

        rotations[idx - 1] = -rotations[idx]

    # main부터 오른쪽으로 전파
    for idx in range(main, 3):
        if not check_polarity(magnets, idx, idx + 1):
            break

        rotations[idx + 1] = -rotations[idx]

    return rotations


def solve(magnets, orders):
    for number, direction in orders:
        main = number - 1 # 직접 돌릴 자석 = main

        # 1. 모든 자석의 회전 방향을 먼저 결정한다.
        rotations = get_rotations(magnets, main, direction)

        # 2. 결정된 방향대로 실제 회전을 적용한다.
        for idx, rotation in enumerate(rotations):
            if rotation == 1:
                turn_right(magnets, idx)
            elif rotation == -1:
                turn_left(magnets, idx)

    return get_score(magnets)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    k = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]
    orders = [list(map(int, input().split())) for _ in range(k)]
    score = solve(magnets, orders)
    print(f"#{test_case} {score}")
