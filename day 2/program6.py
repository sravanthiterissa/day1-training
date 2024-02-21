#write a python program to print reverse of a number
#while loop
n=int(input())
reverse=0
while n > 0:
    digit=n%10
    reverse=reverse*10+digit   #take example 168
    n//=10                     #168/10= 8remainder,digit =8,add digit to reverse*0,so reverse=8,168//10=16
print(reverse)                 #16/10= 6rem,digit=6,add digit to 8*6,so rrverse=8 6, 16//10=1   
                               # 1/10=1 rem ,add digit to reverse so reverse=8 6 1,1//10=0(qutioent)


    
 
