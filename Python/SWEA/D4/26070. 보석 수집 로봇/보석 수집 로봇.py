dir_r = (0,1,0,-1)
dir_c = (1,0,-1,0)

def find_jewel(grid):
    jewels = {}
    for r in range(1,n-1):
        for c in range(1,n-1):
            val = grid[r][c]
            if val != 0:
                jewels[val] = (r,c)
    return jewels

def simulation(grid, jewels):
    r,c = 0,0
    rotate = 0 # 회전한 횟수
    target_num = 1 # 찾아야할 보석
    d = 0 # 현재 방향

    n = len(grid)
    m = len(jewels)

    while target_num <= m:
        tr, tc = jewels[target_num]
        # 현재 위치에 보석이 있으면 수집하고 다음 target
        if (r, c) == (tr, tc):
            target_num += 1
            continue

        nr = r + dir_r[d]
        nc = c + dir_c[d]
        nd = (d + 1) % 4

        if nd == 0:
            jewel_on_right = r == tr and tc > c
        elif nd == 1:
            jewel_on_right = c == tc and tr > r
        elif nd == 2:
            jewel_on_right = r == tr and tc < c
        else:
            jewel_on_right = c == tc and tr < r

        # 테두리거나 현재 방향 우측에 보석이 있으면 우회전
        if not (0 <= nr < n and 0 <= nc < n) or jewel_on_right:
            d = nd
            rotate += 1

        r += dir_r[d]
        c += dir_c[d]
    return rotate

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    jewels = find_jewel(grid)
    print(f'#{test_case} {simulation(grid, jewels)}')

