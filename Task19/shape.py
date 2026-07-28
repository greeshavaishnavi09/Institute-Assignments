class Circle:
    def pay(Self,r):
        print(f"required area to construct a circle:{r}")
       
class Rectangle:
    def pay(Self,width,height):
        print(f"required area to construct a circle:{width}")
        print(f"required area to construct a circle:{height}")  

class Triangle:
    def pay(Self,base,height):
        print(f"required area to construct a circle:{base}")
        print(f"required area to construct a circle:{height}")  

# make function
def draw(draw,r):
    draw.pay(r) 
def area(area,r):
    area.pay(r)   

def draw(draw,width):
    draw.pay(width) 
def area(area,width):
    area.pay(width)

def draw(draw,height):
    draw.pay(height) 
def area(area,height):
    area.pay(height)

def draw(draw,base):
    draw.pay(base) 
def area(area,base):
    area.pay(base)








# create objects

c= Creditcard()
d= Debitcard()
u = Upi()

make_payement(c,500)
make_payement(d,500)
make_payement(u,500)

print(c.pay(100))
print(d.pay(500))
print(u.pay(300))