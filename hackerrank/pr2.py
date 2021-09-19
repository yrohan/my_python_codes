def appendToS(string_s,string_op):
    return string_s + string_op

def deleteK(string_s,k):
    return string_s[:len(string_s)-k]
    
def printK(string_s,k):
    try:
        print(string_s[k-1])
    except:
        print("K is ",k)
        print("Length of string is ",len(string_s))
        print(string_s)

def undo(prev_s):
    if len(prev_s)>1:
        return prev_s[len(prev_s)-1]
    else:
        return prev_s[0]
    
    
S = ""
saved_S = []
saved_S.append(S)
op = []
for i in range(int(input())):
    op.append(input())


for x in range(len(op)):
    if op[x] != '4':
        if op[x].split(' ')[0] == '1':
            S = appendToS(S,op[x].split(' ')[1])
            saved_S.append(S)
        if op[x].split(' ')[0] == '2':
            k = int(op[x].split(' ')[1])
            S = deleteK(S,k)
            saved_S.append(S)
        if op[x].split(' ')[0] == '3':
            k = int(op[x].split(' ')[1])
            printK(S,k)
    else:
        saved_S.pop()
        S = undo(saved_S)
        
    
