# 숫자 n개를 리스트로 입력받아 최솟값을 구하는 프로그램을 만들어 보세요.


def find_min(a):
    n = len(a)
    min_v = a[0]
    for i in range(1, n):
        if a[i] < min_v:
            min_v = a[i]
    return min_v


n_count = int(input("리스트에 넣을 숫자 개수: "))
num_list = []
for i in range(n_count):
    num_list.append(int(input(str(i+1)+"번째 수:")))
print(find_min(num_list))