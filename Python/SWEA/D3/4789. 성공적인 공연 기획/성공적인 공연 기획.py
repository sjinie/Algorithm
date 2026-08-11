T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    audience = input()

    count = 0
    # 지금까지 박수친 사람
    hired = 0
    # 고용한 사람

    # for i in arr
    # 박수치는데 필요한 사람이 i명, arr[i]만큼 박수친 사람에 추가
    #
    for i in range(0,len(audience)):
        if count < i :
            hired += i-count
            #지금까지 박수친 사람이 i보다 작으면 그 차이만큼 고용할 사람에 추가
            count = i
            #이후 박수친 사람을 i로 설정
        count += int(audience[i])
        #arr[i]만큼 박수친 사람에 추가
    print(f'#{test_case} {hired}')
