n = int(input())
gb_name = []
gb_code = []
for i in range(n):
    gb_name.append(input())

for i in range(n):
    str1 = ""
    for j in range(len(gb_name[i])):
        str1 = str1 + gb_name[i][j] * (ord(gb_name[i][j].lower())-ord('a')+1)
    rev_str = "".join(reversed(str1))
    gb_code.append(rev_str)

for i in range(n):
    print(gb_code[i])