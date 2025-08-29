import turtle as t
from numpy.random import choice
import numpy as np

def drawSquare(turtle:t.Turtle, pixel_size):
    '''
    Makes turtle draw an square of side size equal equal to pixel_size. 
    '''
    for _ in range(4):
        turtle.forward(pixel_size)
        turtle.right(90)

def dashed_line(turtle:t.Turtle, n:int, l1:float=10, l2:float=10):
    '''
    Makes turtle draw a dashed line of l1 pixels coloured+l2 pixels blank n times.
    '''
    if type(n)==int:
        for _ in range(n):
            turtle.pendown()
            turtle.forward(l1)
            turtle.penup()
            turtle.forward(l2)
    else:
        print("Error: n must be an integer")

def draw_polygon(turtle:t.Turtle, n:int=3, l:float=30):
    '''
    Makes turtle draw a polygon with n sides of length l
    By default n=3, l=30
    '''
    poly_angle = 360/n
    for _ in range(n):
        turtle.forward(l)
        turtle.right(poly_angle)

def rand_walk(turtle:t.Turtle, steps:int=100, step_lenght:float=20,
              colors:list=["lightpink", "lightskyblue", "palegreen", "moccasin", "thistle"],
              weights:dict={"u":1,"d":1,"r":1,"l":1}):
    '''
    Gets turtle make a random walk.
    By default 100 setps of length=20px in black color are made.
    Weights sets the probability of going into a given direction in each step.
    '''
    angles = {"u":90,"d":270,"r":0,"l":180}
    #List with each direction appearing the number of times set by weights
    dirs = [angles[key] for key in weights.keys() for _ in range(weights[key])]
    for i in range(steps):
        random_color = choice(colors)
        turtle.pencolor(random_color)
        turtle.pensize(width=10)

        random_angle = choice(dirs)
        turtle.setheading(random_angle)
        turtle.forward(step_lenght) 
        print(f"Step {i}")
