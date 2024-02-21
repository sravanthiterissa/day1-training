#write a python program to check whether the number is strong number or not using functions?
#strong number 145=1!+4!+5!=145= 1+24+120=145( sum of factorials of individual digits)

def strong(n):
    x,sum=n,0
    while n > 0:
        digit=n%10
        fact=1
        for i in range(1,digit+1):
            fact*=i
        sum+=fact
        n//=10
    if sum==x:
        print("strong")              #return "strong"
    else:
        print("not strong")           #return "not strong"
n=int(input())
strong(n)                             #print(strong(n))
    


















    
