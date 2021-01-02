def solution(bridge_length, weight, truck_weights):
    from collections import deque

    bridge = deque([])
    truck_weights = deque(truck_weights)
    num = len(truck_weights)
    cnt = 0
    finish = []
    left = weight

    while len(finish)!=num:

        if len(truck_weights) != 0:
            truck = truck_weights.popleft()
            
        else:
            truck = 0

        if len(bridge)==bridge_length:
            finished = bridge.pop()
            left+=finished
            if finished != 0:
                finish.append(finished)

        bridge.appendleft(truck)
        cnt += 1
        left-=truck

        if left < 0: 
            truck = bridge.popleft()
            truck_weights.appendleft(truck)
            bridge.appendleft(0)
            left += truck
            
    
    return cnt

#통과
#sum()은 o(n) 시간복잡도를 가지므로 매번 반복시 시간초과가 날 수 밖에 없음!
#다리 위 트럭 무게의 합보다는 남은 가능한 무게를 비교하는게 시간복잡도 측면에서 더 나음!