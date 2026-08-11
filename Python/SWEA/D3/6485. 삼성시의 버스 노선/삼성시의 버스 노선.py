T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    bus_stops = [0]*5001
    arr = []
    for _ in range(n):
        a, b = map(int,input().split())
        # 버스 노선 하나를 받음
        for stop in range(a,b+1):
            bus_stops[stop] += 1
            #버스 노선 하나를 읽어서 출발지부터 도착지까지 버스도착횟수 +1    
    
    p = int(input())
    for _ in range(p):
        idx = int(input())
        arr.append(bus_stops[idx])
        #답변해야할 버스정류장 번호를 입력받아 해당 번호의 정류장 도착횟수를 배열로 저장
    print(f"#{test_case}", *arr)