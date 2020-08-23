def sort_reverse(a):
    n = len(a)
    for i in range(n-1):
        max_idx = i
        for j in range(i+1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]


d = [2, 4, 5, 1, 3]
sort_reverse(d)
print(d)