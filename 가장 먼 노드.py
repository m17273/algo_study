def solution(n, vertex):
    import collections

    distance = {i:0 for i in range(1, n+1)}
    edge = collections.defaultdict(list)
    
    for n1, n2 in vertex:
        edge[n1].append(n2)
        edge[n2].append(n1)

    q = collections.deque(edge[1])
    
    cnt = 1
    while q:
        for i in range(len(q)):
            num = q.popleft()
            
            if distance[num] == 0:
                distance[num] = cnt

                for i in edge[num]:
                    q.append(i)
        
        cnt +=1
    answer = list(distance.values())
    answer.pop(0)

    max_num = max(answer)
    answer_cnt = 0

    for i in answer:
        if i == max_num:
            answer_cnt += 1
    
    return answer_cnt  
    
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))