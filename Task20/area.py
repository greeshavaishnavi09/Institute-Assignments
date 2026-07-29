class Area:
    def calculate(self,length,breadth=None):
        if breadth is None:
            return length * length
        return length * breadth

obj = Area() 
print(obj.calculate(5))
print(obj.calculate(5, 10))  
