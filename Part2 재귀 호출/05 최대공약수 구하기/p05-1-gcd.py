# 최대 공약수 구하기
# 입력: a, b
# 출력: a와 b의 최대공약수

"""
-최대공약수 알고리즘
1. 두 수 중 더 작은 값을 i에 저장한다.
2. i가 두 수의 공통된 약수인지 확인한다.
3. 공통된 약수이면 이 값을 결괏값으로 돌려주고 종료한다.
4. 공통된 약가 아니면 i를 1만큼 감소시키고 2번으로 돌아가 반복한다.(1수은 모든 정수의 약수이므로 i가 1이 되면 1을 결괏값으로 돌려 주고 종료한다.

"""

def gcd(a,b):
    i = min(a,b)
    while True:
        if a%i==0 and b%i==0:
            return i
        i = i - 1

print(gcd(1,5))
print(gcd(3,6))
print(gcd(60,24))
print(gcd(81,27))