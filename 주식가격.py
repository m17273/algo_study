def solution(prices):
    import collections 

    prices_ = collections.deque(prices)
    answer = []

    while (len(prices_) != 1):

        num = 0
        a = (prices_).popleft()

        for i in range(len(prices_)):
            if prices_[i] < a:
                num = 0
                answer.append(i+1)
                break
            else:
                num +=1
                continue

        if num != 0:
            answer.append(num) 
                
    answer.append(0)
    return answer

print(solution([1,2,3,2,3]))


#정확성테스트는통과 벗 효율성통과 ㄴㄴ