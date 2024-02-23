#using oops concept?
class student:
    def __init__(self,name,age,sec):       #constructor method which executes/intializez when object is created
        self.name=name                     #self= used to represent an object which is not created/ locality of given variable 
        self.age=age
        self.sec=sec
        print(name,age,sec)
obj=student("sravanthi","20","ece-a")
obj1=student("terissa","19","ece-s")

