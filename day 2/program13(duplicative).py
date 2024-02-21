#to remove concecutive duplicative  in a strings
'''s1=input()
s2=""
for i in range (len(s1)):
    if s2[i]!=s2[i+1]:
        s1+=s2[i]
print(s2)'''     #o/p is  error index out of range   


s1=input()
s2=s1[0]
for i in range (1,len(s1)):
    if s1[i-1]!=s1[i]:
        s2+=s1[i]       #terissa== terisa
print(s2)     
