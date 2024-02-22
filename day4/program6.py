#to print sum of the coloumns in a matrix
r,c=int(input()),int(input())
l,sum=[],0
for i in range (r):
        l.append(tuple(map(int,input().split())))
for i in l:
    sum+=i[c-3]    #c-3 for 1st coloumn, c-2 for 2nd coloumn, c-1 for 3rd coloumn
print(sum)    
     
