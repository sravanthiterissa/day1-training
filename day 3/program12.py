#to remove duplicates in a list?
l=list(map(int,input().split()))
l2=[]
for i in l:
       if i not in l2:               #1 2 3 3 3 4 4 5 5 = [1, 2, 3, 4, 5]
           l2.append(i)
print(l2)       
       
