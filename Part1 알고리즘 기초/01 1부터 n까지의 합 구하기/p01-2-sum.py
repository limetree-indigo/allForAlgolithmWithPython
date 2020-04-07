# 1부터 n까지 연속한 숫자의 합을 구하는 알고리즘 1
# 입력: n
# 출력: 1부터 n 까지의 숫자를 더한 값


def sum_n(n):
    return n * (n + 1) // 2


print(sum_n(10))    # 1부터 10까지의 합
print(sum_n(100))   # 1부터 100까지의 합
