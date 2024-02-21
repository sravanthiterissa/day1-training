#strings
s1,s2=map(str,input().split())
s3=""
for i in s2:     # data structues=  srucures
    if i  not in s1:
        s3+=i   # the strings not in s1 add to s3
print(s3)
        
        
        
