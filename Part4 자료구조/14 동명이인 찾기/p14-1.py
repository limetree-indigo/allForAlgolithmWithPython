# 두 번 이상 나온 이름 찾기
# 입력: 이름이 n개 들어 있는 리스트
# 출력: n개의 이름 중 반복되는 이름의 집합

def find_same_name(a):
    # 1단계: 각 이름이 등장한 횟수를 딕셔너리로 만듦
    name_dict = {}
    for name in a:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1
    # 2단계: 만덜어진 딕셔너리에서 등장 횟수가 2 이상인 것을 결과에 추가
    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)

    return result

name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name))

name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name2))