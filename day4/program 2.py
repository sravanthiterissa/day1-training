#to print sum of the given matrix?
'''r,c=int(input("rows:")),int(input("coloums:"))
l=[]
for i in range (r):
        l.append(list(map(int,input().split())))
print(l)'''


# sum
'''r,c=int(input("rows:")),int(input("coloums:"))
l=[]
for i in range (r):
        l.append(list(map(int,input().split())))   
print(l)
s=0
for i in l:
    s+=sum(i)
print(s)'''    

# matrix
r,c=int(input("rows:")),int(input("coloums:"))
l=[]
for i in range(r):
        l.append(list(map(int,input().split())))
s=0
for i in l:
    print(i)
    s+=sum(i)
print(s)    
