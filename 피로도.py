from itertools import permutations

def solution(k, dungeons):
    dungeonPermu = permutations(range(1,len(dungeons)+1), len(dungeons))
    temp = []
    kOrigin = k
    

    for i in dungeonPermu:
        cnt = 0
        k = kOrigin

        for j in i:
            if dungeons[j-1][0] <= k:
                k -= dungeons[j-1][1]
                cnt += 1
            else:
                temp.append(cnt)
                break

        if cnt >= len(dungeons):
            return cnt
    
    return max(temp)
        

print(solution(80, [[80,20], [50,40], [30,10]]))