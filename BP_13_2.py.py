from turtle import *
class car:
    def __init__(self,speed,color,model):
        self.speed=speed
        self.color=color
        self.model=model
        self.turtle=Turtle()
        self.turtle.shape("car.gif")

    def drive(sellf):
        self.turtle.forward(self.speed)

    def left_turn(self):
        self.turtle.left(90)

register_shape("car.gif")
mycar=car(200,"red", "E-class")
for i in range(100):
    myCar.drive()
    mycar.left_turn()
