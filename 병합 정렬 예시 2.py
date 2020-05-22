def merge_sort(a):
    n = len(a)

    if n<=1:
        return

    mid = n//2
    g1 = a[:mid]
    g2 = a[mid:]

    merge_sort(g1)
    merge_sort(g2)

    i1 = 0
    i2 = 0
    ia = 0

    while i1< len(g1) and i2<len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]#입력된 값의 인덱스를 바꿈
            ia +=1
            i1 +=1
            
        else:
            a[ia] = g2[i2]
            ia += 1
            i2 +=1

    while i1<len(g1): #무조건 작을 수 밖에 없음 = 빈 리스트가 될때까지 반복
        a[ia] = g1[i1]
        i1 += 1
        ia += 1

    while i2<len(g2): #무조건 작을 수 밖에 없음 = 빈 리스트가 될때까지 반복
        a[ia] = g2[i2]
        i2 += 1
        ia += 1

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(d)
print(d)
        

            

    
