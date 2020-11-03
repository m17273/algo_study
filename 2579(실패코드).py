num = int(input())

stair = []
result = []

for _ in range(num):
    stair.append(int(input()))


stair.insert(0,0)
sequence = 0
i = len(stair)-1

while True:
    
    if i == 1:
        print(sum(result))
        break
    if i == 0:
        print(sum(result))
        break

    elif i == len(stair)-1:
        if stair[i] + stair[i-1] >= stair[i] + stair[i-2] or stair[i] + stair[i-1] == stair[i-2]:
            if sequence == 0:
                result.append(stair[i]+stair[i-1])
                sequence += 1
                i = i-1
            else:
                result.append(stair[i]+stair[i-2])
                sequence = 0
                i = i-2
        else:
            result.append(stair[i]+ stair[i-2])
            i = i-2
   
    else:
        if stair[i] + stair[i-1] >= stair[i] + stair[i-2] or stair[i] + stair[i-1] == stair[i-2]:
            if sequence == 0:
                result.append(stair[i-1])
                sequence += 1
                i = i-1
            else:
                result.append(stair[i-2])
                sequence = 0
                i = i-2
        else:
            result.append(stair[i-2])
            i = i-2
            sequence = 0

