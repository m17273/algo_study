def solution(N, number):

    collection = [[N],[N+N,N-N, N*N, N//N,int(str(N)*2)]]
    if N == number:
        return 1
        
    for i in range(3,9):
        for j in range(1, (i)+1):


            target1 = collection[j-1]
            target2 = collection[(i-j)-1]
            tmp =[]

            for num1 in target1:
                for num2 in target2:

                    plus = num1+num2 
                    minus = num1-num2
                    multiple = num1*num2
                    if num2 != 0:
                        divide = num1//num2

                    if plus > 0 and plus not in tmp:
                        tmp.append(plus)
                    if minus > 0 and minus not in tmp:
                        tmp.append(minus)
                    if multiple > 0 and multiple not in tmp:
                        tmp.append(multiple)
                    if divide > 0 and divide not in tmp:
                        tmp.append(divide)

            tmp.append(int(str(N)*i))
            
            if number in tmp:
                return i
            collection.append(tmp)

    return -1

print(solution(1,1121))
