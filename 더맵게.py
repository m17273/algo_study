# 통과
# 힙: 최대/최소값을 효율적으로 찾기 위해 고안된 완전 이진 트리(O(logn))
# 노드 왼쪽부터 채워지며, 최소힙 기준 왼쪽 자식 노드 < 오른쪽 자식 노드
# 파이썬의 경우, heapq 모듈을 통해 쉽게 구현 가능(최소힙 형태 정렬)

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
        



