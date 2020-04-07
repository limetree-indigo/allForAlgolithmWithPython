# 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 프로그램을 for 반목문으로 만들 어보세요.
# 예를 들어 n = 10이라면 1^2 + 2^2 + 3^2 + --- + 10^2 = 385를 계산하는 프로그램입니다.
# 계산 복잡도 => 2n번 실행되지만 복잡도는 O(n)


def sum_sq(n):
    result = 0
    for i in range(1, n+1):
        result += i*i

    return result


print(sum_sq(10))
print(sum_sq(100))