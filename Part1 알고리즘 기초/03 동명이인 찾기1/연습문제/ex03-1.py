# n명 중 두명을 뽑아 짝을 짓는다고 할 때 짝을 지울 수 있는 모든 조합을 출력하는 알고리즘을 만들어 보세요.
# 예를 들어 입력이 리스트 ['Tom', 'Jerry', 'Mike']라면 다음과 같은 세 가지 경우를 출력합니다.
# Tom - Jerry
# Tom - Mike
# Jerry - Mike


def match_name(a):
    n = len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            print(a[i],'-', a[j])


name = ["Tom", "Jerry", "Mike"]
match_name(name)
print()
name2 = ["Tom", "Jerry", "Mike", "Jane"]
match_name(name2)