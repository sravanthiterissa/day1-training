# to print the factorial of a given number?

def fact(n):
    if n<1:
        return 1
    else:
        return n*fact(n-1)       # 5!=120(5*4*3*2*1)
n=int(input())
print(fact(n))


