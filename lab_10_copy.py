### copy for experimentation with moving fish

import turtle
import random
import time
turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
SQUARE_SIZE=20
START_LENGTH = 1

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

fishtemplate = turtle.clone()
fishtemplate.shape("square")

fish1=fishtemplate.clone()
fish1.hideturtle()
fish1.direction='Up'
fish1_stamps = []
fish1_poses = []


def random_goto(fish):
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_X/2/SQUARE_SIZE)-1

    fish_x=random.randint(min_x,max_x)*SQUARE_SIZE
    fish_y=random.randint(min_y,max_y)*SQUARE_SIZE

    fish.goto(fish_x,fish_y)

def new_stamp(fish, stamp_list, pos_list):
    #i wanna get the current pos of the fish
    fish_pos = fish.pos()
    #and then make it appear in the pos list
    pos_list.append(fish_pos) 
    #find and save the stamp ID so i can remove it
    #later on when the fish moves        
    r=fish.stamp()
         
    stamp_list.append(r)
    
def remove_last_stamp(fish, stamp_list, pos_list): #BTW i know its a long name, i couldn't find any better
    old_stamp = stamp_list.pop(0) # get the ID of the last piece of body
    fish.clearstamp(old_stamp) # erase this last piece of body from the screen
    pos_list.pop(0) # remove last piece of the body position from the pos list

def move(fish, stamp_list, pos_list):
    #get the pos and save it so that i will be able to change it
    my_pos = fish.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    #if pos is up/down/left/right i want to change the y pos by using
    #square size (20)
    if fish.direction == "Up":
        fish.goto(x_pos, y_pos + SQUARE_SIZE)
   
    elif fish.direction=="Down":
        fish.goto(x_pos, y_pos - SQUARE_SIZE)

    elif fish.direction=="Left":
        fish.goto(x_pos-SQUARE_SIZE, y_pos)

    elif fish.direction=="Right":
        fish.goto(x_pos+SQUARE_SIZE, y_pos)


    #remove the last stamp of the fish to make it "move"
    #TBH functions are not too bad
    remove_last_stamp(fish, stamp_list, pos_list)
    #after i remove the last stamp i make the next stamp. thanks functions :P
    new_stamp(fish, stamp_list, pos_list)

   #where is my fish's new position???
    new_pos = fish.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    #ok now i know where it is

    
    #like in the snake, i want the game to stop once the fish hits the
    #edges of the screen
    if new_x_pos >= RIGHT_EDGE:
         fish.direction="Left"

    if new_y_pos<=DOWN_EDGE:
        fish.direction="Up"

    if new_x_pos<=LEFT_EDGE:
        fish.direction="Right"

    if new_y_pos>=UP_EDGE:
        fish.direction="Down"


random_goto(fish1)
new_stamp(fish1, fish1_stamps, fish1_poses)
move(fish1, fish1_stamps, fish1_poses)
move(fish1, fish1_stamps, fish1_poses)
move(fish1, fish1_stamps, fish1_poses)
move(fish1, fish1_stamps, fish1_poses)

'''


turtle.ontimer(apper_fish,1500)
    
for number in range(4):
    
apper_fish()

starttime=time.time()
while True:
  apper_fish()
  time.sleep(5 - ((time.time() - starttime) % 5))
  
if robot.pos() in fish_pos:
    print('game over! you lost!')
    quit()

"""
#function that makes new stamp for the fish

"""



#and finally, the move function
"""
    if len(trash_stamps)<=6:
        make_trash()
"""

#now use the move!
'''


turtle.mainloop()
