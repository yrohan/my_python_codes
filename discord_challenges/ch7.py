for i in range(int(input())):
    inp = input()
    res = [addr for addr in inp.split(' ') if all(x in "0123456789ABCDEF" for x in ''.join(addr.split('-')))][0]
    print(res)
