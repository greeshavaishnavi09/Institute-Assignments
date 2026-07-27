class Transport:

    # Parent Method
    def move(self):
        print("Transport is moving")


class Bus(Transport):

    def __init__(self):
        super().__init__()


class Train(Transport):

    def __init__(self):
        super().__init__()


b1 = Bus()
t1 = Train()

print("Bus")
b1.move()

print("Train")
t1.move()