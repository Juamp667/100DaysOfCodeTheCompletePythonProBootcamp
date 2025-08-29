import turtle as t

#First the window where the turtle lives is created
win = t.Screen() 

#Then the turtle (playing character) is created
#The shape parameter set the shape of the turtle out of a predefined set of values (although new can be added)
jim = t.Turtle(shape="turtle")

#Every turtle is initialized with a black ben down. Lets work with that
jim.pencolor("red")


def drawSquare(turtle:t.Turtle, pixel_size):
    '''
    Makes turtle draw an square of side size equal equal to pixel_size  
    '''
    for _ in range(4):
        turtle.forward(pixel_size)
        turtle.right(90)

drawSquare(jim,100)

#The following line prevents the window to close until it's clicked
win.exitonclick()