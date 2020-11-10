def solution(skill, skill_tree):
    skill_list = list(skill)
    num = 0
    cnt = 0

    for i in range(len(skill_tree)):
        

        tmp_tree = list(skill_tree[i])
        tmp = list(range(num, tmp_tree))
        check = False


        while tmp:
            a = tmp.pop(0)
    

            for i in tmp_tree:
                if a == i:
                    check = True
                    continue
                else:
                    check=False
                    num = tmp.index(a)
        if check:
            cnt += 1
       
    return cnt

print(solution('CBD', ["BACDE", "CBAF", "AECB", "BDA"]))

