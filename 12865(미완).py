<<<<<<< HEAD
import sys

n, k = map(int, sys.stdin.readline().split())

items = {}



for i in range(n):
    w, v = map(int, sys.stdin.readline().split())

    if w not in items:
        items[w] = [v]
    else:
        if v in items[w]:
            w_ = w + w
            items[w_] = items.pop(w)
            items[w_][0] += v
        else:
            items[w].append(v)

items_weight = sorted(list(items.keys()))
itmes_value_total = []
tempt = []


for i in range(len(items)):
    if items_weight[i] > k:
        continue
    if items_weight[i] == k:
        itmes_value_total.append(max(items[items_weight[i]]))
    if items_weight[i] < k:
        plus = k - items_weight[i]
        if plus in items_weight and plus != items_weight[i]:
            tempt.append(max(items[plus]))
            tempt.append(max(items[items_weight[i]]))
            itmes_value_total.append(sum(tempt))

            plus_ = plus
            tempt = []
            for j in range(len(items_weight)):
                if items_weight[j] < plus_ and items_weight[j] != items_weight[i]:
                   plus_ -= items_weight[j]
                   tempt.append(max(items[items_weight[j]]))

            if len(tempt)>0:
                tempt.append(max(items[items_weight[i]]))
                itmes_value_total.append(sum(tempt))
            else:
                pass
        else:
            plus_ = plus
            for j in range(len(items_weight)):
                if items_weight[j] < plus_ and items_weight[j] != items_weight[i]:
                   plus_ -= items_weight[j]
                   tempt.append(max(items[items_weight[j]]))
            if len(tempt)>0:
                tempt.append(max(items[items_weight[i]]))
                itmes_value_total.append(sum(tempt))
            else:
                itmes_value_total.append(max(items[items_weight[i]]))

print(max(itmes_value_total))


=======
import sys

n, k = map(int, sys.stdin.readline().split())

items = {}



for i in range(n):
    w, v = map(int, sys.stdin.readline().split())

    if w not in items:
        items[w] = [v]
    else:
        if v in items[w]:
            w_ = w + w
            items[w_] = items.pop(w)
            items[w_][0] += v
        else:
            items[w].append(v)

items_weight = list(items.keys())
itmes_value_total = []
tempt = []


for i in range(len(items)):
    if items_weight[i] > k:
        continue
    if items_weight[i] == k:
        itmes_value_total.append(max(items[items_weight[i]]))
    if items_weight[i] < k:
        plus = k - items_weight[i]
        if plus in items_weight and plus != items_weight[i]:
            tempt.append(max(items[plus]))
            tempt.append(max(items[items_weight[i]]))
            itmes_value_total.append(sum(tempt))

            plus_ = plus
            tempt = []
            for j in range(len(items_weight)):
                if items_weight[j] < plus_ and items_weight[j] != items_weight[i]:
                   plus_ -= items_weight[j]
                   tempt.append(max(items[items_weight[j]]))

            if len(tempt)>0:
                tempt.append(max(items[items_weight[i]]))
                itmes_value_total.append(sum(tempt))
            else:
                pass
        else:
            plus_ = plus
            for j in range(len(items_weight)):
                if items_weight[j] < plus_ and items_weight[j] != items_weight[i]:
                   plus_ -= items_weight[j]
                   tempt.append(max(items[items_weight[j]]))
            if len(tempt)>0:
                tempt.append(max(items[items_weight[i]]))
                itmes_value_total.append(sum(tempt))
            else:
                itmes_value_total.append(max(items[items_weight[i]]))

print(max(itmes_value_total))


>>>>>>> 110271555a90c65dbfb55deb605fb23ae037233a
