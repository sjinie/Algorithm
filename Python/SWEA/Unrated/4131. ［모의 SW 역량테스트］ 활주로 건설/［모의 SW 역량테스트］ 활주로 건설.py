# 배열을 받아서 활주로 놓으면서 끝까지 갈 수 있는지
def runway(arr, x):
    #경사로 놓아져있는지
    wedge = [False] * len(arr)

    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        if diff == 0: # 평지
            continue
        if abs(diff) >= 2: # 높이 2 이상 차이나면 무조건 불가
            return False

        elif diff == 1:  # 오르막
            start = i + 1 - x
            if start < 0:
                return False
            for j in range(start, i + 1):
                if (arr[j] != arr[i] or wedge[j]):
                    return False
            for j in range(start, i + 1):
                wedge[j] = True
        elif diff == -1:  # 내리막
            end = i + x
            if end >= n:
                return False
            for j in range(i + 1, end + 1):
                if (arr[j] != arr[i + 1] or wedge[j]):
                    return False
            for j in range(i + 1, end + 1):
                wedge[j] = True
    return True

#행단위, 열단위로 활주로 건설 가능한지 count
def solve(x):
    answer = 0
    for r in range(n):
        if runway(grid[r],x):
            answer += 1
        if runway([grid[c][r] for c in range(n)],x):
            answer += 1
    return answer

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    n, x = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    print(f'#{test_case} {solve(x)}')