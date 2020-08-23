def get_name(s_info, find_no):
    if find_no in s_info:
        return s_info[find_no]
    else:
        return '?'


sample_info = {39: "Justin", 14: "John", 67: "Mike", 105: "Summer"}

print(get_name(sample_info, 105))
print(get_name(sample_info, 777))