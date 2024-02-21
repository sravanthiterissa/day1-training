# strong number using strings and reccursion?

'''def fact(n):
    if n<1:
        return 1
    else:
        return n*fact(n-1)
def strong(x):
    s=str(x)
    sum=0
    for i in s:
        sum+=fact(int(i))
    if sum == x:
        return "strong number"
    else:
        return "not a strong number"
x=int(input())
print(strong(x))'''
#  strong numbers in a range using reccursion and functions

def fact(n):
    if n<1:
        return 1
    else:
        return n*fact(n-1)
def strong(x):
    s=str(x)
    sum=0
    for i in s:
        sum+=fact(int(i))
    if sum == x:
        print(x)
a,b=int(input()),int(input())
for i in range(a,b+1):
    strong(i)
