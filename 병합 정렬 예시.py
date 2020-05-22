def merge_sort(a):
    #종료조건 - 입력리스트 그래로 돌려주면서 재귀 호출 종료
    n = len(a)
   
    if n <= 1:
        return a
   #전체 리스트 절반으로 나눠서 두 그룹으로 재귀호출로 병합정
    mid = n // 2 
    g1 = merge_sort(a[:mid]) 
    g2 = merge_sort(a[mid:])
    
    result = []
    #g1과 g2에 자료가 남아있을 때까지 반복
    while g1 and g2:  
        if g1[0] < g2[0]: 
          
            result.append(g1.pop(0))
        else:
            
            result.append(g2.pop(0))

   #아직 남아있는 애들을 결과에 추가
    # 빈 애들은 while을 바로 지나감
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d))
