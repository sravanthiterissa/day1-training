#pizza
#nf=no of friends, ns=no.of slices,#np=no of pizzas
'''nf,ns=map(int,input().split(" "))  
np=nf*ns                           
if np%4==0:
    print(np//4)
else:
    print((np//4)+1)'''

     

'''nf,ns=map(int,input().split(" "))  
if nf*ns%4==0:
    print(nf*ns//4)
else:
    print((nf*ns//4)+1)'''


import math
nf,ns=map(int,input().split(" "))  
np=nf*ns
y=math.ceil(np/4)
print(y)


            
