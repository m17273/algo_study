def solution(n):
    cnt = 0
    for i in range(1,n+1):
        
        tmp = [i]
        for j in range(i+1, n+1):
            
            target = tmp[-1] + j 
            
            if target < n:
                tmp.append(target)
                continue
            elif target > n:
                break
            else:
                cnt += 1

    return cnt+1


print(solution(15))
                
                






        
