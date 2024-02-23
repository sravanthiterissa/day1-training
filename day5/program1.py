# write a python program to take dictionary as a input and print keys and values of a dictionary?
'''n=int(input("enter no of items:"))
d={}
for i in range(n):
    key=input("key:")
    value=input("value:")
    d[key]=value
print(d)'''

#another method(using methods)

n=int(input("enter no of items:"))
d={}
for i in range(n):
    key=input("key:")
    value=input("value:")
    d[key]=value
for i in d:
   print("key:{} value:{}".format(i,d[i]))
for i in d.keys():
    print(i)
for i in d.values():
    print(i)


#types to print "print"statements
'''seperating by comma=  print("key:",i,"","value:",d[i])     #key: 1  value: hi
f function=           print(f"key:{i} value:{d[i]}")           #key:1 value:hi
format function =     print("key:{} value:{}".format(i,d[i]))  #key:1 value:hi'''
