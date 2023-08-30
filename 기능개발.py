import math

def solution(progresses, speeds):
    temp = []
    maxDay = 0

    for i in range(len(progresses)):
        leftover = 100 - progresses[i]
        leftday = math.ceil(leftover/speeds[i])
        
        if len(temp) == 0:
            temp.append(1)
            maxDay = leftday

        else:
            if leftday <= maxDay:
                temp[-1] += 1
            else:
                maxDay = leftday
                temp.append(1)
    print(len(progresses))
    return temp


print(solution([95,90,99,99,80,99], [1,1,1,1,1,1]))



