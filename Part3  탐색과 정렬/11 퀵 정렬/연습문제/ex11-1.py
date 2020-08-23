# 거품 정렬
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)

def bubble_sort(a):
    n = len(a)
    while True:
        changed = False     # 자료를 앞뒤로 바꾸었는지 여부
        # 자료를 훑어보면서 뒤집힌 자료가 있으면 바꾸고 바뀌었다고 표시
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                changed = True
        if not changed:
            return

d = [2, 4, 5, 1, 3]
bubble_sort(d)
print(d)