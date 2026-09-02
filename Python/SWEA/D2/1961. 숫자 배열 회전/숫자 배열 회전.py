def turn90(arr):
    arr2 = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            arr2[r][c] = arr[n-c-1][r]
    return arr2

def solve(arr):
    answer = []
    answer.append( turn90(arr) )
    answer.append( turn90(turn90(arr)) )
    answer.append( turn90(turn90(turn90(arr))) )
    print(f'#{test_case}')
    for i in range(n):
        print(*( "".join(map(str, answer[j][i])) for j in range(3) ))

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 3):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    solve(arr)