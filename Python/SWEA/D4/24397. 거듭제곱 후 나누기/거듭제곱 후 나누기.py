import math
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    X, Y, Z = map(int, input().split())

    num1 = pow(X, Y, Z * 1000)
    num2 = num1 // Z
    num3 = (num1 % Z) * 1000 // Z

    # X**Y / Z >= 100인지 log로 판정
    log_value = Y * math.log10(X) - math.log10(Z)
    three_digits = log_value >= 2.0

    if three_digits:
        integer_part = f"{num2:03d}"
    else:
        integer_part = str(num2)

    print(f"{integer_part}.{num3:03d}")