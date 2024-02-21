#write a python program to print amstrong numbers in a range using strings ans functions?
def amst(n,m):
   for i in range(n,m+1):
       s=str(i)
       sum=0 
       for j in s:
           sum+=int(j)**len(s) 
       if str(sum) == s:
           print(i)
n,m=int(input()),int(input())  
amst(n,m)
       
