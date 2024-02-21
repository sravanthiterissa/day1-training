#to print the sum of odd composite numbers in a given range?
#composite= numbers which are not prime numbers

'''def composite(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count > 2:
        return 1
    else:
        return 0
a,b=int(input()),int(input())   # o/p= all composite numbers between range 
l=[]
for i in range(a,b+1):
    flag=composite(i)
    if flag == 1:
            l.append(i)
print(sum(l))
print(l)'''

# to print only odd composite numbers
'''def composite(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count > 2:
        return 1
    else:
        return 0
a,b=int(input()),int(input())   # o/p=  only odd composite numbers between range 
l=[]
for i in range(a,b+1):
    if i%2!=0:
        flag=composite(i)
        if flag == 1:
            l.append(i)
print(sum(l))
print(l)'''

# to print only even composite numbers
def composite(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count > 2:
        return 1
    else:
        return 0
a,b=int(input()),int(input())   # o/p=  only even composite numbers between range 
l=[]
for i in range(a,b+1):
    if i%2==0:
        flag=composite(i)
        if flag == 1:
            l.append(i)
print(sum(l))
print(l)



