T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    cards = list(map(int,list(input())))
    max_count = 0
    frequent = 0
    for i in range(len(cards)):
        num = cards[i]
        cnt = 0
        for j in range(len(cards)):
            if(num == cards[j]):
                cnt += 1
                if(cnt >= max_count):
                    max_count = cnt
                    frequent = max(frequent, num)
    print(f'#{test_case} {frequent} {max_count}')