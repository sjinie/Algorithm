dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def explode(arr, r, c):
    if arr[r][c] == 0:
        return 0
    num = arr[r][c]
    arr[r][c] = 0
    exploded = 1
    # 자기 자신 폭파 처리
    for n in range(1, num):
        for i in range(4):
            nr = r + dir[i][0] * n
            nc = c + dir[i][1] * n
            if 0 <= nr < H and 0 <= nc < W:
                if arr[nr][nc] != 0:
                    exploded += explode(arr, nr, nc)
    return exploded
	# 폭파시킨 벽돌 수 return

def gravity(arr):
    for c in range(W):
        col = list(''.join(str(arr[r][c]) for r in range(H)).replace('0', ''))
        # 문자열로 합치고 0 없앤뒤에 아래에서부터 다시 채우기
        for r in range(H - 1, -1, -1):
            if col:
                arr[r][c] = int(col.pop())
            else:
                arr[r][c] = 0

def shoot(shot, arr, remain):
    if remain == 0 or shot == N:
        return remain
    # 남은 벽돌이 없거나 구슬 다 쐈으면 종료
    answer = remain
    for c in range(W):
        new_arr = [row.copy() for row in arr]
        for r in range(H):
            if new_arr[r][c]:
                exploded = explode(new_arr, r, c)
                gravity(new_arr)
                answer = min(answer,shoot(shot + 1, new_arr, remain - exploded))
                break
                #dfs로 열마다 구슬 떨어뜨리면서 모든 경우 완전탐색하고 최솟값 return
    return answer
        
T = int(input())
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = []
    for _ in range(H):
        arr.append(list(map(int, input().split())))
    # 입력
    remain = 0
    for r in range(H):
        for c in range(W):
            if arr[r][c] != 0:
                remain += 1
    answer = shoot(0, arr, remain)
    print(f"#{test_case} {answer}")