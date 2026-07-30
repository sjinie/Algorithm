T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    times = []
    for _ in range(N):
        times.append(int(input()))
    #print(N,M,time)
    
    left = 0 
    right = min(times)*M
    # 총 소요시간 T는 아무리 커도 제일 빠른 사람 한명만 일을 한 시간보다는 빠름
    
    while left < right:
        mid = (left+right) // 2
        count = 0
        # 이진탐색 => T = 중간값(mid)일때, 총 몇명 검사를 마쳤나
       	# 각자 정해진 시간 mid동안, (총시간)//(한명 검사하는데 걸리는시간) = (총 시간 동안 검사한 사람)이고 이것의 합은 
		#  for i in range(N){ mid//times[i] }
		# 이걸 M이랑 비교해서 크면, 시간이 충분한것. 작으면, 시간이 부족한것 => 이진탐색
        for time in times:
            count += mid // time
        if count >= M:
            right = mid
        else:
            left = mid +1
    answer = left
    print(f'#{test_case} {answer}')
    
