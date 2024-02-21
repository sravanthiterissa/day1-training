#write a python program to check whether the given number is prime number or not?
#for loop #factors exist if the remainder is 0

'''n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("it is not a prime")'''
      

#leaving itself as a factor
'''n=int(input())
count=0
for i in range(1,n):
    if n%i==0:
        count+=1
if count==1:
    print("prime")
else:
    print("it is not a prime")'''
     
#2 to n(between values)if not divisible print prime
'''n=int(input())
for i in range(2,n):
    if n%i==0:
        print(" not a prime")
        break
else:
    print("prime")'''
#decrease iterations
'''n=int(input())
for i in range(2,(n//2)+1):
    if n%i==0:
        print(" not a prime")
        break
else:
    print("prime") '''
#decrease itearations by sqaring
n=float(input())
for i in range(2,(n**0.5)+1):
    if n%i==0:
        print(" not a prime")
        break
else:
    print("prime")


 #while
n=int(input())
while i < (2,(n**0.5)+1):
    if n%i==0:
        print(" not a prime")
        break
    i+=1
else:
    print("prime")   
     
