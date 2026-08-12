#  방향벡터
dir = [(-1,0),(1,0),(0,-1),(0,1)] #상하좌우

# DFS
def dfs(core_idx, acc_core_connected, acc_wire_length):
    global max_core_connected, min_wire_length

    # 남은 Core를 모두 연결해도 기존 최댓값보다 작다면 중단
    if acc_core_connected + (len(cores) - core_idx) < max_core_connected:
        return

    if core_idx == len(cores):
        if acc_core_connected > max_core_connected:
            max_core_connected = acc_core_connected
            min_wire_length = acc_wire_length
        elif acc_core_connected == max_core_connected:
            min_wire_length = min(min_wire_length, acc_wire_length)
        return

    r, c = cores[core_idx]
    for dr, dc in dir:
        nr, nc = r, c
        wire_length = 0

        while True:
            nr += dr
            nc += dc
            if not (0 <= nr < N and 0 <= nc < N):
                dfs(core_idx + 1,acc_core_connected + 1,acc_wire_length + wire_length)
                break

            if arr[nr][nc] != 0:
                break

            arr[nr][nc] = 2
            wire_length += 1

        #백트래킹 (전선 연결 불가능한 경우에 원상복구)
        nr, nc = r, c
        for _ in range(wire_length):
            nr += dr
            nc += dc
            arr[nr][nc] = 0

    # Core를 연결하지 않는 경우
    dfs(core_idx + 1, acc_core_connected, acc_wire_length)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [] #전체 배열
    cores = [] #전원에 연결해야 하는 코어 좌표
    for r in range(N): 
        row = list(map(int,input().split()))
        for c in range(N):
            if(row[c] != 0):
                if(0 < r < N-1 and 0 < c < N-1): #border(전원)에 인접한 코어들 제외
                    cores.append((r,c)) 
        arr.append(row)
    # 입력

    max_core_connected = 0
    min_wire_length = N**2

    dfs(0, 0, 0)
    #print(*arr, sep='\n')
    print(f'#{test_case} {min_wire_length}')