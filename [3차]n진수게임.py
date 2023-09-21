# 실패
# 테스트케이스 1/2/3만 통과

def primenumList(n,t,m):
    originNum = list(range(t*m))
    primenum = []
    alphabetList = ['A', 'B', 'C', 'D', 'E', 'F']

    revNumber = ''

    for i in originNum:
        target = i

        if target == 0:
            primenum.append(str(target))
        
        elif 10 <= target <= 15:
            primenum.append(alphabetList[target-10])
        else:
            while target > 0:
                target, mod = divmod(target, n)
                revNumber += str(mod)

            revNumberFinal = revNumber[::-1]
            
            if len(revNumberFinal) > 1:
                for j in revNumberFinal:
                    primenum.append(j)
            else:
                primenum.append(revNumberFinal)
            revNumber = ''
    
    return primenum

def solution(n,t,m,p):
    primenum = primenumList(n,t,m)
    cnt = p
    result = ''

    while len(result) != t:
        result += primenum[cnt-1]
        cnt += m

    return result

print(solution(2,4,2,1))