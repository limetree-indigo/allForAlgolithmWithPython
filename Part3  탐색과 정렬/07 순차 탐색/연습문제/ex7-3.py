def search_name(s_no, s_name, find_no):
    n = len(s_no)
    for i in range(n):
        if s_no[i] == find_no:
            return s_name[i]

    return '?'

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", 'John', "Mike", "Summer"]

print(search_name(stu_no, stu_name, 39))