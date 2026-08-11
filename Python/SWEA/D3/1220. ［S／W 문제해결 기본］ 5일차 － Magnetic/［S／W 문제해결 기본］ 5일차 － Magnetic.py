T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(input().split()))
    cnt = 0
    for col in zip(*arr):
        cnt += ''.join(col).replace('0','').count('12')
    print(f'#{test_case} {cnt}')