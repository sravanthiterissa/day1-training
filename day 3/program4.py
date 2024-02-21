#write a python program to make encryption and decryption with a key value using functions?
#encryption= giving  codes to char, decryption= obtaining char from codes
#chr for decrypt(-) , ord for encrypt(+)
def encryption(s,k):
    s1=""
    for i in s:
        x=ord(i)+k
        s1+=chr(x)
    print(s1)    
def decryption(s,k):
    s1=""
    for i in s:
        x=ord(i)-k
        s1+=chr(x)
    print(s1) 
k=int(input("enter key value:"))     #encrypt= sravs=key value=3=    vudyv(+3)
s=input("enter string:")            #decrypt= sravs key vlaue= 3=    po^sp(-3)
op=input("select operation:")
if op == "encrypt":
    encryption(s,k)
elif op == "decrypt":
    decryption(s,k)
else:
    print("inproper operation")
    
        
