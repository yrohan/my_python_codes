import numpy
import random

credit=[4,4,3.5,4,4]
sum_cr=sum(credit)
Iterations = 20
result=[]
x=[]

for i in range(Iterations):
    chromosome=[random.randint(6,9) for j in range(len(credit))]
    x.append(chromosome)

for i in range(Iterations):
   res=0
   for j in range(len(credit)):
       res=res+credit[j]*x[i][j]
   res=res/sum_cr
   if(res>8):
    result.append(x[i])

print "\nMinimum C.G. Required = ",min(result)