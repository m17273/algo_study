n = int(input())
member = []

for i in range(n):
    member.append(list(map(str, input().split())))

member_fin = sorted(member, key=lambda x:x[0])

def merge_sort(a):
    n = len(a)

    if n<=1:
        return a

    mid = n//2
    g1 = list(a[:mid])
    g2 = list(a[mid:])

    i1 = 0
    i2 = 0
    ia = 0

    while i1<len(g1) and i2<len(g2):
        if g1(int([i1][0]))<g2(int([i2][0])):
            a[ia] = g1[i1]
            ia += 1
            i1 += 1

        elif g1(int([i1][0])>g2(int[i2][0])):
            a[ia] = g2[i2]
            i2 += 1
            ia += 1

    while i1<len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1

    while i1<len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1

merge_sort(member_fin)

    
for j in range(n):
    print(member_fin[j][0], member_fin[j][1])
