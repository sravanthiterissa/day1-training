#a shopping mall having 5%discount for men and 7%discount for women and
#individual discount for each item they puchase is 3*no of items customers purchase caculate the total bill?

'''sp1,dm=map(int,input().split())
sp2,dw=map(int,input().split())
sp3=int(input())
di=3*int(input())
ap1=sp1-(sp1*(dm/100))
ap2=sp2-(sp2*(dw/100))
print(ap1)
print(ap2)
print(sp3-(sp3*(di/100)))
print(ap1+ap2+di)'''
#using dictionary

d={}
n=int(input("enter no of items: "))
for i in range(n):
    k=input("enter item: ")
    v=int(input("enter item prize:"))
    d[k]=v
l=[]
for i in d:
    l.append(d[i]-d[i]*(3*n)/100)
g=input("enter gender: ")
if g =="mae":
    bill=sum(l)-sum(l)*5/100
else:
    bill=sum(l)-sum(l)*7/100
j=0
print("items - prices: discount-prices")
for i in d:
      print(f"{i}-{d[i]}:{l[j]}")
      j+=1
else:
    print("*"*20)
print(f"total bill:{bill}")  
         
         
