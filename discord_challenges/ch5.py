n = int(input())
val = []
for i in range(n):
    val.append(input())
for i in range(n):
    res = int('0xFFFFFF', 16)-int(val[i], 16)
    print('0x'+hex(res)[2:].zfill(6))
