#통과

import math

# 10진수 > k진수로 변경하는 함수 (반환값 : str)
def numberChange(n, k):
    revNumber = ''

    while n > 0:
        # divmod(n, k) >> (몫, 나머지)를 튜플형태로 반환(몫은 정수부만 반환 = //)
        n, mod = divmod(n, k)
        revNumber += str(mod)

    return revNumber[::-1]
    # 역순인 진수를 뒤집어줘야 원래 변환 하고자하는 숫자를 받을 수 있음
    # 문자열을 뒤집어서 반환하고 싶을 땐, [::-1] 활용 >>
    # ex) [3:0:-1] >> 3번 인덱스부터 1번 인덱스까지 역순으로 출력

# 소수인지 판별하는 함수
def primenumChecker(n):
    n = int(n)
    
    if n != 1:
        # 1과 자기 자신을 제외한 약수가 존재하면? >> 해당 수는 소수가 아님
        # 따라서 약수의 성질(대칭적으로 짝을 이룸)을 활용하여, 자기자신의 제곱근 범위까지만 확인하면 됨
        
        for i in range(2, int(math.sqrt(n))+1): # 2부터 n의 제곱근까지의 숫자
            if n % i == 0: # 나눠떨어지는 숫자가 있으면 n은 소수가 아님
                return False
        return True
    else:
        return False

def solution(n, k):
    changedNum = numberChange(n, k)
    currentNum = ''
    cnt = 0

    for i in changedNum:

        if i != '0':
            currentNum += i

        else:
            if currentNum == '':
                continue

            else:   
                checker = primenumChecker(currentNum)
                
                if checker == True:
                    cnt += 1

                currentNum = ''

    # for문이 끝났음에도 판별을 하지 않은 currentNum이 남아있으면, 해당 부분까지 판별하기 위한 별도 조건문
    if currentNum != '':
        checker = primenumChecker(currentNum)
        
        if checker == True:
                cnt += 1

    return cnt

print(solution(437674, 3))