import numpy
import os
import time

m1=numpy.loadtxt("C:\\Users\\Linux\\Downloads\\list_of_companies.csv",dtype='string',delimiter=',',skiprows=0)
n=(m1.size/m1[0].size)
f1=open('load_companies.js','w')
f1.write("use companies \n")
f1.write("show collections\n")
f1.write("db.company.insert([")
for i in range(1,n):
    f1.write("{")
    for j in range(0,m1[0].size):
        if(j==0 or j==5):
            f1.write(" "+m1[0][j]+":"+m1[i][j]+",\n")
        else:
            f1.write(" \""+m1[0][j]+"\":\""+m1[i][j]+"\",\n")
    if(i==n-1):
        f1.write("}")
    else:
        f1.write("},")

f1.write("]);")
f1.close()

os.system("start mongod")
time.sleep(5)
os.system("mongo < load_companies.js")
