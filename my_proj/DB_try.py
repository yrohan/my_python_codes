import numpy

m1=numpy.loadtxt("C:\\Users\\Linux\\Documents\\names.csv",dtype='string',delimiter=',',skiprows=0)

print(m1.size)
print(m1[0].size)

f1=open('load_names.txt','w')
f1.write("db.names.insert([")
for i in range(1,(m1.size/m1[0].size)):
    f1.write("\n { \n \""+m1[0][0]+"\":\""+m1[i][0]+"\", \n\""+m1[0][1]+"\":\""+m1[i][1]+"\" \n} ")

f1.write("])")
f1.close()