from nltk.corpus import inaugural

fname=inaugural.fileids()
length1=len(fname)
my_year=[]
for i in range(0,length1):
   my_year.append(fname[i][0:4])

for i in range(0,length1):
    print my_year[i]+" : "+fname[i]





