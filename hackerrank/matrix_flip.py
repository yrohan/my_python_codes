matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
m1 = []
m2 = []
m3 = []
m4 = []
n = int(len(matrix)/2)
for i in range(n):
    m1 += [matrix[i][:n]]
    m2 += [matrix[i][n:][::-1]]
for i in range(n, 2*n):
    m3 += [matrix[i][:n]]
    m4 += [matrix[i][n:][::-1]]
m3 = m3[::-1]
m4 = m4[::-1]
res = 0
for i in range(n):
    for j in range(n):
        res += max(m1[i][j], m2[i][j], m3[i][j], m4[i][j])
print(res)