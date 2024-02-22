#to print sum of maximum and miniumum elements in tuple matrix?

'''r,c=int(input("rows:")),int(input("coloums:"))
l=[]
for i in range (r):
        l.append(tuple(map(int,input().split())))
for i in l:
    print(i)'''

#min and max
'''r,c=int(input("rows:")),int(input("coloums:"))
l=[]
for i in range (r):
        l.append(tuple(map(int,input().split())))
min,max=1000,0       
for i in l:
    print(i)
    for j in i:
        if j > max:
            max=j
        if j < min:
            min=j
print(max+min)'''
# tuple in tuple
r,c=int(input("rows:")),int(input("coloums:"))
l=[]
for i in range (r):
        l.append(tuple(map(int,input().split())))
min,max=1000,0
print(tuple(l))
for i in l:
    print(i)
    for j in i:
        if j > max:
            max=j
        if j < min:
            min=j
print(max+min)     

            
