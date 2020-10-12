def solution(scoville, K):
    import heapq
    
    scoville_sort = sorted(scoville)

    first = scoville_sort[0:2]
    del scoville_sort[0:2]
    cnt = 0

    while True:
        if sum(first) <= (K*2):
            heapq.heapify(first)
            a = first.pop(0)
            b = first.pop(0) 

            first.append(a+(b*2))
            
            if len(scoville_sort)>=1:
                first.append(scoville_sort.pop(0))
                cnt += 1
            else:
                if sum(first) >= K*2:
                    cnt += 1
                    return cnt
                else:
                    return -1
        else:
            return cnt
        

print(solution([1,1,2], 3))








