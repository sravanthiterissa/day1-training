#to print sum of odd numbers in a range?

n,m=int(input()),int(input())
l=[i for i in range(n,m+1) if i%2!=0]   # 1 to 10= 1+3+5+7+9=25
print(sum(l))
