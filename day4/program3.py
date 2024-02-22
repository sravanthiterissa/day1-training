#product of elements inside the matrix?

'''r,c=int(input("rows:")),int(input("coloums:"))
l=[]
for i in range (r):
        l.append(list(map(int,input().split())))    #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]=  1  2 3 4 5 6 7 8 9         
print(l)
for i in l:
    for j in i:
        print(j)'''

# product
'''r,c=int(input("rows:")),int(input("coloums:"))
l=[]
for i in range (r):
        l.append(list(map(int,input().split())))   # o/p= 362880(product )
product=1
for i in l:
    print(i)
    for j in i:
        product*=j
print(product)    '''

# another method
r,c=int(input("rows:")),int(input("coloums:"))
l=[0]*r
for i in range (r):
        l[i]=list(map(int,input().split()))   
product=1
for i in l:
    print(i)
    for j in i:
        product*=j
print(product)    
        
