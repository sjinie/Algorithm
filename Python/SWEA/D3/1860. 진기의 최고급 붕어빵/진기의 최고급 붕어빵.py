#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arrivals = list(map(int, input().split()))
    stock = 0
    result = True
    
    arrivals = sorted(arrivals)

    for i in range(N):
        t = arrivals[i]
        stock = (t//M)*K - i
        if (stock <= 0):
            result = False

    print(f"#{test_case} {'Possible' if result else 'Impossible'}")
