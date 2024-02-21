#to print n natural numbers using reccurssion?

'''def printing(n):
    if n<1:
        return 1
    else:
        print(n)
        printing(n-1)      # o/p= 10 9 8 7 6 5 4 3 2 1
n=10
printing(n)'''


'''def printing(n):
    if n<1:
        return 1s
    else:
        printing(n-1)      # o/p= 1 2 3 4 5 6 7 8 9 10
        print(n)
n=10
printing(n)'''

def printing(n):
    if n<1:
        return 1
    else:
         printing(n-1)
         print(n)
n=int(input())
printing(n)
