# write a python program to check whether the year is a leap year or not?
#condition for leap year- it should be divisible by 4 and 400
#it should NOT be divisible by 100

'''a=int(input())
if a%400==0:
      print("it is a leap year")
elif a%4==0 and a%100!=0:
    print("it is  a leap year")
else:
    print("not a leap year")'''



a=int(input())
if a%400==0 or a%4==0 and a%100!=0:
      print("it is a leap year")
else:
    print("not a leap year")
