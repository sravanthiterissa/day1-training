#to print factorial of a given number using class and methods?
'''class s:
    def fact(self,n):
        f=1
        for i in range(1,n+1):
            f*=i
        print(f)
obj=s()
obj.fact(int(input()))'''
#using constructor

class s:
    def __init__(self,data):
        self.data=data
        self.fact(data)
    def fact(self,n):    
        f=1
        for i in range(1,n+1):
            f*=i
        print(f)
obj=s(int(input()))
    
    
