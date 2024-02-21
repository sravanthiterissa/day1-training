#percentage discount
c1,c2,d1,d2=map(int,input().split(" "))
fa=c1-c1*d1//100
fb=c2-c2*d2//100
if fa <  fb:
    print("first")
elif fa > fb:
    print("second")
else:
    print("any")
