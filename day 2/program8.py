
#write a python program to print amstrong numbers in a range using function?
def amst(n,m):
   for i in range(n,m+1):   #100,1001
       sum=0
       x=i  #i= 100 initially
       while i > 0:
           temp=i%10
           sum+=temp**3 # 1*3+0*3+0*3=1
           i//=10
       if sum == x:
           print(x)
n,m=int(input()),int(input())  #100,1000
amst(n,m)
       
       
















  
   
