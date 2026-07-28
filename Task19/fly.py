class Bird():
    def fly(self):
        print("bird is flying")

class Aeroplane():
    def fly(self):
        print("aeroplane is flying")

def flying_obj(obj):
    obj.fly()

def display(obj):
    obj.fly()

b = Bird()
a=  Aeroplane()

display(b)
display(a)