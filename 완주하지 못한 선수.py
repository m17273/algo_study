<<<<<<< HEAD
def solution(participant, completion):
    a = sorted(participant)
    b = sorted(completion)

    for i in range(len(b)):
        if a[i] != b[i]:
            return a[i]
        else:
            continue
    return a[-1]

=======
def solution(participant, completion):
    a = sorted(participant)
    b = sorted(completion)

    for i in range(len(b)):
        if a[i] != b[i]:
            return a[i]
        else:
            continue
    return a[-1]

>>>>>>> 110271555a90c65dbfb55deb605fb23ae037233a
