#first repeating character?
s=input()
for i in s:
    if s.count(i) > 1:      #count>1=ptints 1st letter
        print(i)
        break
else:
    print('.')
