def solution(people, limit):
    people_sorted = sorted(people)
    tmp_list = []
    cnt = 0
    

    while people_sorted:
        
        one = people_sorted.pop(0)
        tmp_list.append(one)

    
        if sum(tmp_list)>limit:
            tmp_list.pop()
            people_sorted.insert(0, one)
            cnt += 1
            tmp_list=[]


    return cnt+1
print(solution([70, 50, 80], 100))

    
    
#실패..후ㅜㅜ후후후후ㅜ후핳