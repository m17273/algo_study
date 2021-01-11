# import sys
# T = int(sys.stdin.readline())

# def Fly(possible, departure, start):
#     for i in range(len(distance)-1):
#         for j in range(len(possible)):
#             if distance[i] == departure and distance[i] + possible[j] in distance[:len(distance)-1]:
#                 if distance[i] not in answer:
#                     answer.append(distance[i])
#                     if distance[i] + possible[j] != departure:
#                         start = possible[j]
#                         departure = distance[i]+possible[j]
#                         possible = sorted([start-1, start, start+1], reverse=True)
#                         Fly(possible, departure, start)
#                     else:
#                         if start > 2:
#                             answer.pop()
#                         else:
#                             return


            

# for _ in range(T):
#     x,y = map(int, sys.stdin.readline().split())
#     answer = []
#     distance = list(range(x,y+1))
#     answer.append(distance.pop(0))

#     start = 1
#     finish = distance[-2]
#     departure = distance[0]
#     possible = sorted([start-1, start, start+1], reverse=True)
#     Fly(possible, departure, start)
#     print(len(answer))
 
import sys

T = int(sys.stdin.readline())

def Fly():
    global departure
    global start
    possible = sorted([start-1, start, start+1], reverse=True)

    for i in range(len(possible)):
        if departure + possible[i] in distance[:len(distance)-1] and departure+possible[i] > answer[-1]:
            if departure+possible[i] != finish:
                start = i
                departure += possible[i]
                if departure not in answer:
                    answer.append(departure)
                
            else:
                if i < 3:
                    if departure+i not in answer:
                        answer.append(departure + i)
                    break


for _ in range(T):
    x,y = map(int, sys.stdin.readline().split())
    distance = list(range(x, y+1))
    start = 1
    finish = distance[-2]
    answer = []

    for i in range(len(distance)):
        if i == 0:
            continue
        elif i == 1:
            departure = distance[i]
            answer.append(distance[i])
            Fly()
        else:
            Fly()
    print(len(answer))
    

