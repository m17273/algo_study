num = int(input())
li = []

for i in range(num):
    Input = str(input())
    if Input not in li:
        li.append(Input)

list_fin = sorted(li)

def quick_sort(a):
    n = len(a)

    if n<=1:
        return a

    pivot = a[n//2]

    g1 = []
    g2 = []
    g3 = []

    for i in range(n):
        if len(a[i])< len(pivot):
            g1.append(a[i])
        elif len(a[i]) > len(pivot):
            g2.append(a[i])
        else:
            g3.append(a[i])
           
            
    return g1 + g2 + g3


quick_sort(list_fin)
print(list_fin)
