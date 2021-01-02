def solution(priorities, location):
    from collections import deque

    priorities = deque(priorities)
    printer = deque(list(range(len(priorities))))
    cnt = 0

    while True:
        max_num = max(priorities)
       
        for i in range(1,len(priorities)):
            if priorities[0] < priorities[i]:
                tmp = priorities.popleft()
                priorities.append(tmp)
                tmp = printer.popleft()
                printer.append(tmp)
                break
        if printer[0] == location:
            return cnt+1 

        elif priorities[0] == max_num :
            priorities.popleft()
            printer.popleft()
            cnt += 1
        
    

print(solution([1,2,3],0))
        


            