children,candies=int(input()),int(input()),
if candies >=children: #if candies are more than children no need to buy extra candies so np=0
    np=0
else:
    x=children-candies  #np=no of packets need to buy, x=difference(no of candies needed)
    if x%4==0:          
        np=x//4
    else:
        np=(x//4)+1
print(np)        

