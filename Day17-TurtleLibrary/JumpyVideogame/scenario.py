import turtle as t
from numpy import random
#Platform's class is created with inheritance form Turtle class
class Platform(t.Turtle):
    def __init__(self, x:float=0, y:float=0, length:float=5, width:float=0.5,shape = "classic", undobuffersize = 1000, visible = False, color="black"):
        super().__init__(shape, undobuffersize, visible)

        #Set platform's shape and color
        self.shape("square")    
        self.shapesize(stretch_len=length, stretch_wid=width)
        self.fillcolor(color)

        #Set platform's position
        self.penup()
        self.speed(0)
        self.setpos(x,y)     
        self.showturtle()

#Test code
if __name__=="__main__":
    s = t.Screen()
    p = Platform()
    p.setpos(x=100,y=50)
    s.exitonclick()
    print(p.shapesize())