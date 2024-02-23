#input 5
#output {1:"composite",2:"prime",3:"prime",4:"composite",5:"prime"}
'''def isprime(m):
    for i in range(2,m):
        if m%i==0:
            return "composite"   #o/p= 5 = {1: 'prime', 2: 'prime', 3: 'prime', 4: 'composite', 5: 'prime'}
    else:
        return "prime"
n=int(input())
d={}
for i in range(n):
    k=i+1
    v=isprime(i+1)
    d[k]=v
print(d)'''
#
def isprime(m):
    for i in range(2,m):
        if m%i==0:
            return "composite"   
    else:
        return "prime"
m=int(input())
'''print(isprime(m)'''
for i in range(m):
      print(i+1,"=",isprime(i+1))
