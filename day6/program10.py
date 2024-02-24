from abc import ABC
class shape(ABC):
            def print(self):
                print("i am a normal method defined inside the abstract class 'shape")
            def calculate_are(self):
                pass
      class rectangle(shape):
          length=5
          breadth=3
          def calculate_area(self):
              return self.length*self.breadth
            rec=rectangle()
            rec.print()
            print("area of a rectangle:",rec
