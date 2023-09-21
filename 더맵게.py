import heapq

def solution(scoville, k):
    cnt = 0
    temp = []

    heapq.heapify(scoville)

    while scoville[0] < k:

        if len(scoville) >= 2:
            while len(temp) != 2:
                minnum = heapq.heappop(scoville)
                temp.append(minnum)

            newScoville = temp[0] + (temp[1]*2)
            heapq.heappush(scoville, newScoville)
            temp = []
            cnt += 1

        else:
            return -1
    
    return cnt    
            
        
print(solution([12,10,9,3,2,1], 7))
        



