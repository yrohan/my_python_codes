n = int(input())
wanted = []
typed = []
for i in range(n):
    wanted.append(input())
    typed.append(input())
for i in range(n):
    pos = False
    for j in range(len(typed[i])):
        if 0 < wanted[i].count(typed[i][j]) <= typed[i].count(typed[i][j]):
            pos = True
        else:
            pos = False
            break
    if pos:
        print("yes")
    else:
        print("no")
