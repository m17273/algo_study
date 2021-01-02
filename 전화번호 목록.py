def solution(phone_book):
    phone_book = sorted(phone_book, key= lambda x: len(x))

    for i in range(len(phone_book)):
        if i == len(phone_book)-1:
            return True

        num = len(phone_book[i])
        for j in range(i+1, len(phone_book)):
            check = phone_book[j][0:num]

            if phone_book[i] == check:
                return False

print(solution(['12', '123', '1235', '567', '88']))

#통과