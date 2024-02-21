#write a python program to remove a duplicates in a given string
s1=input()
s2=""
for i in s1:
    if i not in s2:   #sravanthi == sravnthi
        s2+=i
print(s2)        
    

