def search_all_index(a, x):
    n = len(a)
    result = []
    for i in range(n):
        if a[i] == x:
            result.append(i)

    return result

v = [1, 2, 3, 4, 1, 2, 9, 10]
print(search_all_index(v, 1))
print(search_all_index(v, 9))
print(search_all_index(v, 20))
