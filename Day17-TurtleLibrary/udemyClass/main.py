import turtle as t
import turtleFunctions as tFs

#First the window where the turtle lives is created
win = t.Screen() 

#Then the turtle (playing character) is created
#The shape parameter set the shape of the turtle out of a predefined set of values (although new can be added)
jim = t.Turtle(shape="turtle")


#Test functions
# tFs.drawSquare(jim,30)
# tFs.dashed_line(jim,10.1,15,2)
# tFs.draw_polygon(jim, 6, 30)
jim.speed(0)
tFs.rand_walk(jim, steps=1000, step_lenght=15)

#The following line prevents the window to close until it's clicked
win.exitonclick()