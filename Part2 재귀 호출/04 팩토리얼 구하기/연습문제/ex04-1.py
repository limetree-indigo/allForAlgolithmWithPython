# 문제 1의 1부터 n까지의 합 구하기를 재귀 호출로 만들어 보세요.


def sum_n(a):
    if a < 1:
        return 0
    return a + sum_n(a-1)


print(sum_n(10))
