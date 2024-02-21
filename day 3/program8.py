# to print sum of n natural numbers using recurssion?

'''def printing(n):
    if n<1:
        return 1
    else:
        print(n)
        return n+ printing(n-1)     # o/p= 10 9 8 7 6  5 4 3 2 1 56(sum)
n=int(input())
sum=printing(n)
print(sum)'''

def printing(n):
    if n<1:
        return 1
    else:
        return n+ printing(n-1)     #56(sum)
n=int(input())
sum=printing(n)
print(sum)

