#calling objects in constructor
'''class college:
    def __init__(self,name):
        self.name=name
        self.ece1()
        self.ece2()
    def ece1(self):
        print("this is ece1",self.name)
    def ece2(self):
        print("this is ece2",self.name)
s=input()
obj=college(s)'''

#return
class college:
    def __init__(self):
        print(self.sec1())
        print(self.sec2())
    def sec1(self):
        return "method1"
    def sec2(self):
        return "method2"
obj=college()    
