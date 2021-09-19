for i in range(int(input())):
    inp = input()
    res = ''.join([inp[i+1]*int(inp[i]) for i in range(0,len(inp)-1,2)])
    print(res)