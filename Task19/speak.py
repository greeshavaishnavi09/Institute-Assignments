class Dog:
    def speak(self):
        print("Dog : bow bow")

class Robot:
    def speak(self):
        print("Robot : beep boop")

 # make function

def make_sound(obj):
    obj.speak()

def display(sound):
    sound.speak()

d= Dog()
r = Robot()

display(d)
display(r)


        