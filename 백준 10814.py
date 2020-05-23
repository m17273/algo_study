import sys

n = int(input())
member = []

for i in range(n):
    member.append(list(sys.stdin.readline().split()))

def merge_sort(a):
    n = len(a)

    if n <=1:
        return

    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]

    



