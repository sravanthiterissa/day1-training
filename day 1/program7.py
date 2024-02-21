#finding the low cost tv out of two
#c1,c2=costs of tv, d1,d2 are discounts of tv
c1,c2,d1,d2=map(int,input().split(" "))
if (c1-d1)<(c2-d2):
    print("first")
elif (c1-d1)>(c2-d2):
    print("second")
else:
    print("any")


