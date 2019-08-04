import turtle
import random

fish=turtle.clone()
turtle.hideturtle()

def apper_fish():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_X/2/SQUARE_SIZE)-1

fish_x=random.randit(min_x,max_x)*SQUARE_SIZE
fish_y=random.randit(min_y,max_y)*SQUARE_SIZE
fish.goto(fish_x,fish_y)
