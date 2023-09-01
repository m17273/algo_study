def solution(priorities,location):
    # sorted함수는 오름차순이 기본
    # 내림차순을 적용하기 위해선, 'reverse=True' 매개변수 포함해줄 것 
    prioritiesSorted = sorted(priorities,reverse=True)
    locationList = list(range(len(prioritiesSorted)))
    checker = False
    answer = 0

    while checker != True:
        target = prioritiesSorted.pop(0)

        while True:

            if target != priorities[0]:
                temp1 = priorities.pop(0)
                temp2 = locationList.pop(0)
                priorities.append(temp1)
                locationList.append(temp2)
            
            else:
                if locationList[0] != location:
                    priorities.pop(0)
                    locationList.pop(0)
                    answer += 1
                    break
                else:
                    answer += 1
                    checker = True
                    break
        
    return answer


print(solution([1,1,9,1,1,1], 0))