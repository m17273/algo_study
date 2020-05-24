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

    for i in a:
        if len(i)< len(pivot):
            g1.append(i)
        elif len(i) > len(pivot):
            g2.append(i)
        else:
            g3.append(i)
           
            
    return quick_sort(g1) + g3 + quick_sort(g2)


quick_sort(list_fin)
print(list_fin)
