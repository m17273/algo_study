def solution(n, results):
    check = [[0]*n for _ in range(n)]
    answer = 0

    for winner, loser in results:
        check[loser-1][winner-1] = 1
        check[winner-1][loser-1] = -1

    for i in range(len(check)):
        for j in range(len(check)):
            if check[i][j] == -1:
                tmp = check[j]

                for k in range(len(check)):
                    if tmp[k] == 0 and k!=j:
                        tmp[k] = check[i][k] # = 이랑 ==이랑 잘 구분좀 하쟈ㅜㅜ왜자꾸실수하닝
             
    
   
    for i in range(len(check)):
        cnt = 0
        for j in check[i]:
            if j == 0:
                cnt += 1
        if cnt == 1:
            answer += 1
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
