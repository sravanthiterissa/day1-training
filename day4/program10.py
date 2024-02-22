#set built in functions
#any#all
'''s={1,2,3,0,4}
print(all(s))'''

#frozenset
'''a=frozenset([1,2,3,4])  #o/p= frozenset({1, 2, 3, 4})
print(a)'''

# to check whether the string is panagram(it should contain a to z letters)
import string
s=input()
s=s.lower()
s1=string.ascii_lowercase
if set(s) == set(s1):
    print("panagram")
else:
    print("not")

