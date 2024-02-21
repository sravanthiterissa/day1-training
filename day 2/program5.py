#write a python program to check whether the given number is perfect number or not?
#for loop
n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("perfect number")
else:
    print("it is not a perfect number")
  
