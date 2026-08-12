def move(germs):  # 1시간마다 이동시키기
    moved_germs = []
    for r, c, count, dir_idx in germs:
        nr = r + dir[dir_idx][0]
        nc = c + dir[dir_idx][1]

        # 다음 이동 위치가 padding이면
        if nr <= 0 or nr >= N - 1 or nc <= 0 or nc >= N - 1:
            count = count // 2
            dir_idx = reverse[dir_idx]
            if count == 0:
                continue
        r = nr
        c = nc
        moved_germs.append((r, c, count, dir_idx))
    return moved_germs


def merge(germs):
    # germs 순회하면서 같은 좌표끼리 모으기
    merged = {}
    for r, c, count, dir_idx in germs:
        pos = (r, c)
        # merged[pos] = [sum, max_count, max_dir] 해당 위치의 총 미생물 수, 가장 많은 군집의 미생물 수, 방향
        if pos not in merged:
            merged[pos] = [count, count, dir_idx]
        else:
            merged[pos][0] += count
            if count > merged[pos][1]:
                merged[pos][1] = count
                merged[pos][2] = dir_idx
    merged_germs = []
    for pos in merged:
        new_r = pos[0]
        new_c = pos[1]
        new_count = merged[pos][0]
        new_dir = merged[pos][2]
        merged_germs.append((new_r, new_c, new_count, new_dir))
    return merged_germs


T = int(input())

# 방향벡터
dir = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
reverse = [0, 2, 1, 4, 3]

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    germs = []
    for _ in range(K):
        germs.append(list(map(int, input().split())))
    # 군집(r,c,count,dir)
    for _ in range(M):  # M시간동안 격리
        germs = move(germs)
        germs = merge(germs)

    answer = sum(count for r, c, count, dir_idx in germs)
    print(f"#{test_case} {answer}")
