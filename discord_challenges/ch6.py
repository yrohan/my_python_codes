t = int(input())
inp = []
for i in range(t):
    inp.append(input())
test_str = '2020'
all_substr = list(set([test_str[i:j] for i in range(len(test_str)) for j in range(1, len(test_str)+1)]))
substr = [[x, y] for x in all_substr for y in all_substr if x+y == test_str]
for i in range(t):
    res = False
    for j in range(len(substr)):
        if substr[j][0] != substr[j][1]:
            if substr[j][0] == '' and substr[j][1] in inp[i]:
                res = True
                break
            elif substr[j][1] == '' and substr[j][0] in inp[i]:
                res = True
                break
            elif substr[j][0] in inp[i] and substr[j][1] in inp[i]:
                res = True
                break
        else:
            occ = len([x for x in range(len(inp[i])) if inp[i].startswith(substr[j][0], x)])
            if occ >= 2:
                res = True
    print(str(res))
