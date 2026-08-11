T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, 1+T):
    N = int(input())
    op = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    results = []
    
    def dfs(idx, value):
        if idx == N:
            results.append(value)
            return
        
        for op_idx in range(4):
            if op[op_idx] > 0 :
                op[op_idx] -= 1
                if op_idx == 0:
                    dfs(idx+1, value + nums[idx])
                elif op_idx == 1:
                    dfs(idx+1, value - nums[idx])
                elif op_idx == 2:
                    dfs(idx+1, value * nums[idx])
                elif op_idx == 3:
                    dfs(idx+1, int(value / nums[idx]))
                    # '//' 사용시 음수를 나눌때 정수부만 남는게 아니라 반올림되어버림
                op[op_idx] += 1
    dfs(1,nums[0])
    print(f"#{test_case} {max(results)-min(results)}")