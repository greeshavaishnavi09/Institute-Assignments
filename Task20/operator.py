class Calculation:
    def __init__(self,grade):
        self.grade = grade
        print(self.grade)

    #dunder 
    def __creation__(self,other):
        result = self.grade =  other.grade
        return result 

    def __eq__(self, other):
        result = self.grade == other.grade
        return result

    

s1 = Calculation(80)
s2 = Calculation(40)

print(s1 == s2)







