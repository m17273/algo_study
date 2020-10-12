def solution(bridge_length, weight, truck_weights):
    
    import collections

    deque = collections.deque([0]*(bridge_length))
    available = weight
    cnt = 0
    truck_weights_= collections.deque(truck_weights)

    while truck_weights_:
        truck = truck_weights_.popleft()

        if truck<available:
            
            deque.pop()
            deque.appendleft(truck)
            available -= truck
            cnt += 1
        else:
            while sum(deque) <= truck:
                deque.pop()
                deque.appendleft(0)
                cnt += 1



            deque.pop()
            deque.appendleft(truck)
            available = weight-truck

    cnt += bridge_length
    return cnt


print(solution(2, 10, [7,4,5,6]))
















'''


            available = weight-sum(deque)

            if truck_weights[0] < available:
                truck = truck_weights.popleft()
                deque.pop()
                deque.appendleft(truck)
                cnt += 1
            else:
                deque.popleft()
                deque.appendleft(0)
                cnt += 1


''' 









