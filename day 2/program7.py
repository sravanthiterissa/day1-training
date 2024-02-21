#to check whether the number is amstrong mumber or not
#153= 1*3+5*3+3*3= should be equal to 153,  sum=sum+digit**3

n=int(input())
temp=n
rev=0
while n > 0:
    digit=n%10
    rev=rev+digit**3
    n//=10
if rev== temp:
    print("amstrong")
else:
    print("not an amstrong")
    
